from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from cloud.serializers import FilesListSerializer
from cloud.models import File


class FileListView(ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer


class FileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FilesListSerializer
