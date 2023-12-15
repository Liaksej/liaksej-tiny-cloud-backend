from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import UserDetailsView
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from authentication.views import LoginView, CustomRegisterView
from . import views

router = DefaultRouter()
router.register(r"users", views.UsersViewSet)

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
] + router.urls
