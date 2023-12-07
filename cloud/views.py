import mimetypes
import urllib

from django.http import FileResponse
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response

from cloud.models import File
from cloud.permissions import IsOwner, IsOwnerOrStaff
from cloud.serializers import FilesListSerializer
from cloud.services import save_file, delete_file


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    parser_classes = [MultiPartParser, JSONParser]
    ordering = ["-date_created"]

    def get_permissions(self):
        # Access only to the authenticated users
        return [IsAuthenticated(), IsOwner()]

    def list(self, request, *args, **kwargs):
        # Show files owned by the authenticated user only, even if they don't have any files
        self.queryset = self.queryset.filter(user_id=request.user.id)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        file = self.request.FILES.get("file")
        file_info = save_file(file)

        comment = self.request.POST.get("comment")
        file_name = self.request.POST.get("file_name")

        serializer.save(
            name=file_info["file_name"],
            original_name=file_name,
            file_path=file_info["file_path"],
            file_type=file.content_type,
            user_id=self.request.user.id,
            comment=comment,
            size=file.size,
        )

    def perform_destroy(self, instance):
        delete_file(instance.file_path)

        instance.delete()


class DownloadFileView(RetrieveModelMixin, GenericViewSet):
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def retrieve(self, request, *args, **kwargs):
        try:
            file = open(self.get_object().file_path, "rb")
            mime_type, _ = mimetypes.guess_type(self.get_object().file_type)
            response = FileResponse(file, content_type=mime_type)
            encoded_filename = urllib.parse.quote(self.get_object().original_name.encode("utf-8"))
            response["Content-Disposition"] = f'inline; filename*=UTF-8\'\'{encoded_filename}'
            return response
        except FileNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)