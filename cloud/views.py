from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from cloud.models import File
from cloud.permissions import IsOwnerOrAdmin
from cloud.serializers import FilesListSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer

    def get_permissions(self):
        if self.action == "list" and self.request.user.is_superuser:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsAuthenticated(), IsAdminUser()]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.queryset = self.queryset.filter(user__user=request.user)
        return super().list(request, *args, **kwargs)
