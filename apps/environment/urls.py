from django.urls import path
from apps.environment.views import CameraEnvironmentListView, CameraEnvironmentCreateView, CameraEnvironmentUpdateView, CameraEnvironmentDeleteView

urlpatterns = [
    path("environment/", CameraEnvironmentListView.as_view(), name="environment_list"),
    path("environment/create-environment/", CameraEnvironmentCreateView.as_view(), name="environment_create"),
    path("environment/<int:pk>/update-environment/", CameraEnvironmentUpdateView.as_view(), name="environment_update"),
    path("environment/<int:pk>/delete-environment/", CameraEnvironmentDeleteView.as_view(), name="environment_delete"),
]
