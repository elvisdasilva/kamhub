from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.environment.models import CameraEnvironment


class CameraEnvironmentListView(ListView):
    template_name = "environment/environment.html"
    model = CameraEnvironment
    context_object_name = "camera_environments"


class CameraEnvironmentCreateView(CreateView):
    template_name = "environment/create_environment.html"
    model = CameraEnvironment
    fields = "__all__"
    success_url = reverse_lazy("environment_list")
