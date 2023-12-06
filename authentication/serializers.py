from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from cloud.models import File
from cloud.models import User as CloudUser


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

    @staticmethod
    def get_count_files(instance):
        return File.objects.filter(user_id=instance.id).count()

    @staticmethod
    def get_total_space(instance):
        return File.objects.filter(user_id=instance.id).aggregate(Sum("size"))


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    def validate(self, data):
        if not isinstance(data["first_name"], str):
            raise serializers.ValidationError("First name must be a string")
        if not isinstance(data["last_name"], str):
            raise serializers.ValidationError("Last name must be a string")
        return data

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["first_name"] = self.validated_data.get("first_name", "")
        data_dict["last_name"] = self.validated_data.get("last_name", "")
        return data_dict

    def save(self, request):
        user = super().save(request)
        CloudUser.objects.create(
            user=user,
            path_to_store=f"https://{user.username}.local",
        )
        return user
