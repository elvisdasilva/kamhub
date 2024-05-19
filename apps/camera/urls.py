from django.urls import path
from apps.camera.views import CameraListView, CameraCreateView, CameraUpdateView, CameraDeleteView, StreamView

urlpatterns = [
    path("camera/", CameraListView.as_view(), name="camera_list"),
    path("camera/create-camera/", CameraCreateView.as_view(), name="camera_create"),
    path("camera/<int:pk>/update-camera/", CameraUpdateView.as_view(), name="camera_update"),
    path("camera/<int:pk>/delete-camera/", CameraDeleteView.as_view(), name="camera_delete"),
    path("home/stream/<str:user>/<str:password>/<str:ip>/<int:port>/", StreamView.as_view(), name="stream"),
]
