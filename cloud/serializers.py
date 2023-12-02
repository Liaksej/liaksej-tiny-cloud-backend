from rest_framework import serializers

from cloud.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
