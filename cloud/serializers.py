from rest_framework import serializers

from cloud.models import File
from django.contrib.auth.models import User


class FilesListSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.user.username", read_only=True)

    class Meta:
        model = File
        fields = [
            "id",
            "name",
            "original_name",
            "comment",
            "size",
            "date_created",
            "date_downloaded",
            "user",
            "original_name",
            "file_path",
            "file_type",
        ]

    def __init__(self, *args, **kwargs):
        super(FilesListSerializer, self).__init__(*args, **kwargs)

        request = self.context.get("request")
        if request and request.method == "GET":
            keep_fields = [
                "id",
                "original_name",
                "comment",
                "size",
                "date_created",
                "date_downloaded",
            ]
            drop_fields = set(self.fields.keys()) - set(keep_fields)

            for field_name in drop_fields:
                self.fields.pop(field_name)

        if request and (request.method == "PUT" or request.method == "PATCH"):
            read_only_fields = [
                "id",
                "original_name",
                "size",
                "date_created",
                "date_downloaded",
                "file_type",
                "file_path",
                "user",
            ]

            for field_name in read_only_fields:
                self.fields[field_name].read_only = True
