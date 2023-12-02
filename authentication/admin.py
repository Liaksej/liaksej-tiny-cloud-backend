from allauth.account.models import EmailAddress
from django.contrib import admin
from rest_framework.authtoken.admin import TokenProxy


# Register your models here.
admin.site.unregister(TokenProxy)
