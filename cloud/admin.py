from django.contrib import admin

from cloud.models import File, User


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'original_name', 'file_path', 'date_created', 'date_downloaded', 'comment', 'size', 'file_type', 'public_url')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email', 'password', 'admin', 'pass_to_store')