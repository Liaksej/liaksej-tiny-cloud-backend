from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from cloud.permissions import IsOwnerOrAdmin

# Create your views here.
from cloud.serializers import FilesListSerializer
from cloud.models import File


class FileListView(ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(user__user__username=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user__user__username=self.request.user)


class FileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
    permission_classes = [IsOwnerOrAdmin]
