from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from cloud.models import File


class UserListSerializer(serializers.ModelSerializer):
    count_files = serializers.SerializerMethodField()
    total_space = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "date_joined",
            "last_login",
            "count_files",
            "total_space",
        ]

    def __init__(self, *args, **kwargs):
        super(UserListSerializer, self).__init__(*args, **kwargs)

        request = self.context.get("request")

        if request and (request.method == "PUT" or request.method == "PATCH"):
            for field_name in self.fields:
                if field_name == "is_superuser":
                    continue
                self.fields[field_name].read_only = True

    def get_count_files(self, instance):
        return File.objects.filter(user_id=instance.id).count()

    def get_total_space(self, instance):
        return File.objects.filter(user_id=instance.id).aggregate(Sum("size"))
