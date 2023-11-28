import uuid
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    full_name = models.JSONField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    admin = models.BooleanField()
    pass_to_store = models.TextField()


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_downloaded = models.DateTimeField(auto_now=True)
    comment = models.TextField(null=True, blank=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    public_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

