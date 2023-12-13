import uuid

from rest_framework import serializers

from cloud.models import File


class FilesListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username", read_only=True)
    public = serializers.BooleanField(read_only=False, default=False)

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
            "public_url",
            "public",
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
                "public_url",
                "user",  # TODO: remove this field
            ]
            drop_fields = set(self.fields.keys()) - set(keep_fields)

            for field_name in drop_fields:
                self.fields.pop(field_name)

        if request and request.method == "POST":
            keep_fields = ["comment", "name"]
            self.fields["name"].read_only = True
            drop_fields = set(self.fields.keys()) - set(keep_fields)

            for field_name in drop_fields:
                self.fields.pop(field_name)

        if request and (request.method == "PUT" or request.method == "PATCH"):
            read_only_fields = [
                "id",
                "name",
                "size",
                "date_created",
                "date_downloaded",
                "file_type",
                "file_path",
                "user",
                "public_url",
            ]

            for field_name in read_only_fields:
                self.fields[field_name].read_only = True

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if validated_data.get("public"):
            instance.public_url = str(uuid.uuid4())
        else:
            instance.public_url = None

        instance.save()

        return instance
