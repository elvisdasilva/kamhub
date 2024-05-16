from django.urls import path
from apps.environment.views import CameraEnvironmentListView

urlpatterns = [
    path("environment/", CameraEnvironmentListView.as_view(), name="environment_list"),
]
