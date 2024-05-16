from django.shortcuts import render
from django.views.generic import ListView
from apps.environment.models import CameraEnvironment


class CameraEnvironmentListView(ListView):
    template_name = "environment/environment.html"
    model = CameraEnvironment
    context_object_name = "camera_environments"
