import mimetypes
from urllib import parse as urllib

from django.http import FileResponse
from django.utils.timezone import now
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cloud.models import File
from cloud.permissions import IsOwner, IsOwnerOrStaff
from cloud.serializers import FilesListSerializer
from cloud.services import save_file, delete_file


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    parser_classes = [MultiPartParser, JSONParser]
    ordering = ["-date_created"]
    search_fields = ["original_name"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsOwner()]

        return [IsAuthenticated(), IsOwnerOrStaff()]

    def list(self, request, *args, **kwargs):
        if self.request.query_params and "username" in self.request.query_params.keys():
            self.queryset = self.queryset.filter(
                user__user__username=self.request.query_params.get("username")
            )
            return super().list(request, *args, **kwargs)
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


class FileDownloadMixin:
    @staticmethod
    def download_file(file_obj):
        try:
            file = open(file_obj.file_path, "rb")
            mime_type, _ = mimetypes.guess_type(file_obj.file_type)
            response = FileResponse(file, content_type=mime_type)
            encoded_filename = urllib.quote(file_obj.original_name.encode("utf-8"))
            response["Content-Disposition"] = (
                f"inline; filename*=UTF-8''{encoded_filename}"
            )

            return response
        except FileNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DownloadFileView(FileDownloadMixin, RetrieveModelMixin, GenericViewSet):
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.date_downloaded = now()
        instance.save(update_fields=["date_downloaded"])
        self.check_object_permissions(request, instance)
        return self.download_file(instance)


class PublicFileDownloadView(FileDownloadMixin, RetrieveModelMixin, GenericViewSet):
    queryset = File.objects.all()
    lookup_field = "public_url"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.date_downloaded = now()
        instance.save(update_fields=["date_downloaded"])
        return self.download_file(instance)
