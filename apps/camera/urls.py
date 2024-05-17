from django.urls import path
from apps.camera.views import CameraListView, CameraCreateView

urlpatterns = [
    path("camera/", CameraListView.as_view(), name="camera_list"),
    path("camera/create-camera/", CameraCreateView.as_view(), name="camera_create"),
]
