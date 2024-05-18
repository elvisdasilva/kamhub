from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.environment.models import CameraEnvironment
from django.contrib import messages
from apps.environment.forms import CameraEnvironmentForm


class CameraEnvironmentListView(ListView):
    template_name = "environment/environment.html"
    model = CameraEnvironment
    context_object_name = "camera_environments"


class CameraEnvironmentCreateView(CreateView):
    template_name = "environment/create_environment.html"
    model = CameraEnvironment
    form_class = CameraEnvironmentForm
    success_url = reverse_lazy("environment_list")

    def form_valid(self, form):
        messages.success(self.request, "Ambiente cadastrado com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar ambiente.")
        return super().form_invalid(form)


class CameraEnvironmentUpdateView(UpdateView):
    template_name = "environment/update_environment.html"
    model = CameraEnvironment
    form_class = CameraEnvironmentForm
    success_url = reverse_lazy("environment_list")

    def form_valid(self, form):
        messages.success(self.request, "Ambiente atualizado com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar ambiente.")
        return super().form_invalid(form)


class CameraEnvironmentDeleteView(DeleteView):
    template_name = "environment/delete_environment.html"
    model = CameraEnvironment
    success_url = reverse_lazy("environment_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Ambiente deletado com sucesso.")
        return super().delete(request, *args, **kwargs)
