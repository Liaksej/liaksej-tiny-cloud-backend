from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from cloud.models import File
from cloud.permissions import IsOwner
from cloud.serializers import FilesListSerializer
from cloud.services import save_file, delete_file


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    parser_classes = [MultiPartParser]
    ordering = ["-date_created"]

    def get_permissions(self):
        if self.action not in ["create", "update"] and self.request.user.is_superuser:
            return [IsAuthenticated(), IsAdminUser()]
        return [IsAuthenticated(), IsOwner()]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.queryset = self.queryset.filter(user__user=request.user)
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
