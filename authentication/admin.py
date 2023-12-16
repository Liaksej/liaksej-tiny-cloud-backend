from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.admin import TokenProxy

admin.site.unregister(TokenProxy)
admin.site.unregister(User)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = "__all__"
        field_classes = UserCreationForm.Meta.field_classes


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
    )
