import uuid
from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.


class User(models.Model):
    user = models.OneToOneField(
        AuthUser, on_delete=models.CASCADE, primary_key=True, related_name="clouduser"
    )
    path_to_store = models.URLField(null=False, blank=False)

    @property
    def last_login(self):
        return self.user.last_login

    @property
    def id(self):
        return self.user.id

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def is_active(self):
        return self.user.is_active

    @property
    def is_superuser(self):
        return self.user.is_superuser

    @property
    def username(self):
        return self.user.username


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_downloaded = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    public_url = models.UUIDField(null=True, default=None, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="files",
    )
