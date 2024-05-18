from django.urls import path
from apps.camera.views import CameraListView, CameraCreateView, CameraUpdateView, CameraDeleteView

urlpatterns = [
    path("camera/", CameraListView.as_view(), name="camera_list"),
    path("camera/create-camera/", CameraCreateView.as_view(), name="camera_create"),
    path("camera/<int:pk>/update-camera/", CameraUpdateView.as_view(), name="camera_update"),
    path("camera/<int:pk>/delete-camera/", CameraDeleteView.as_view(), name="camera_delete"),
]
