from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"files", views.FileViewSet)
router.register(r"download", views.DownloadFileView)


urlpatterns = [] + router.urls
