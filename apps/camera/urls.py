from django.urls import path
from apps.camera.views import CameraListView

urlpatterns = [
    path("camera/", CameraListView.as_view(), name="camera_list"),
]
