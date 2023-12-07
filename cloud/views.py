from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cloud.models import File
from cloud.permissions import IsOwner
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
