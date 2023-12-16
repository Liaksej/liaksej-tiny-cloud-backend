from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User as AuthUser, Group
from django.contrib.sites.models import Site

from .models import File, User as CloudUser

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)


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


@admin.register(CloudUser)
class CloudUserAdmin(admin.ModelAdmin):
    list_display = ("pass_to_store",)


class CloudUserInline(admin.StackedInline):
    model = CloudUser
    can_delete = False
    verbose_name_plural = "users"


class UserAdmin(DefaultUserAdmin):
    inlines = (CloudUserInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "get_pass_to_store",
    )

    def get_pass_to_store(self, obj):
        return obj.clouduser.path_to_store

    get_pass_to_store.short_description = "Path To Store"


admin.site.unregister(AuthUser)
admin.site.unregister(CloudUser)
admin.site.register(AuthUser, UserAdmin)
