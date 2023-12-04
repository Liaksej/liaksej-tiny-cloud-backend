from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from cloud.models import File
from cloud.permissions import IsOwnerOrAdmin
from cloud.serializers import FilesListSerializer
from cloud.services import save_file


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action == "list" and self.request.user.is_superuser:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsAuthenticated(), IsAdminUser()]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.queryset = self.queryset.filter(user__user=request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        file = self.request.FILES.get("file")
        file_info = save_file(file)

        comment = self.request.POST.get("comment")

        serializer.save = {
            "name": file_info["file_name"],
            "original_name": file.name,
            "file_path": file_info["file_path"],
            "file_type": file.content_type,
            "user": self.request.user.id,
            "comment": comment,
            "size": file.size,
        }
