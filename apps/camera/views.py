from django.views.generic import ListView, CreateView
from apps.camera.models import Camera
from django.urls import reverse_lazy
from django.contrib import messages


class CameraListView(ListView):
    template_name = "camera/camera.html"
    model = Camera
    context_object_name = "camera"


class CameraCreateView(CreateView):
    template_name = "camera/create_camera.html"
    model = Camera
    fields = "__all__"
    success_url = reverse_lazy("camera_list")

    def form_valid(self, form):
        messages.success(self.request, "Câmera cadastrada com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar câmera.")
        return super().form_invalid(form)
