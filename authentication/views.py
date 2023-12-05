from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2Client
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.registration.views import SocialLoginView, LoginView as BaseLoginView
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from authentication.serializers import UserListSerializer


# Create your views here.
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:3000/"
    client_class = OAuth2Client


class LoginView(BaseLoginView):
    def process_login(self):
        if self.user.is_active and self.user.is_superuser:
            django_login(self.request, self.user)
        elif api_settings.SESSION_LOGIN:
            super().process_login()


class UsersViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    lookup_field = "username"

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    ordering = ["username"]
    permission_classes = [IsAuthenticated, IsAdminUser]
