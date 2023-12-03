from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"files", views.FileViewSet)


urlpatterns = [
    # path("files/", views.FileListView.as_view()),
    # path("files/<str:pk>/", views.FileDetailView.as_view()),
] + router.urls
