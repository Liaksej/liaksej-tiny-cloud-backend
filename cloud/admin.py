from django.contrib import admin

from cloud.models import File, User


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "original_name",
        "file_path",
        "date_created",
        "date_downloaded",
        "comment",
        "size",
        "file_type",
        "public_url",
        "user",
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_login",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
        "username",
        "pass_to_store",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("user")

    def is_active(self, obj):
        return obj.user.is_active

    is_active.admin_order_field = "user__is_active"
    is_active.boolean = True
    is_active.short_description = "Active?"

    def is_superuser(self, obj):
        return obj.user.is_superuser

    is_superuser.admin_order_field = "user__is_superuser"
    is_superuser.boolean = True
    is_superuser.short_description = "Superuser?"
