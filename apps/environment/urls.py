from django.urls import path
from apps.environment.views import CameraEnvironmentListView, CameraEnvironmentCreateView

urlpatterns = [
    path("environment/", CameraEnvironmentListView.as_view(), name="environment_list"),
    path("environment/create-environment/", CameraEnvironmentCreateView.as_view(), name="environment_create"),
]
