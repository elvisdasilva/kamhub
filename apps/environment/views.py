from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.environment.models import CameraEnvironment
from django.contrib import messages


class CameraEnvironmentListView(ListView):
    template_name = "environment/environment.html"
    model = CameraEnvironment
    context_object_name = "camera_environments"


class CameraEnvironmentCreateView(CreateView):
    template_name = "environment/create_environment.html"
    model = CameraEnvironment
    fields = "__all__"
    success_url = reverse_lazy("environment_list")

    def form_valid(self, form):
        messages.success(self.request, "Ambiente cadastrado com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar ambiente.")
        return super().form_invalid(form)
