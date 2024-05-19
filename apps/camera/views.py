from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from apps.camera.forms import CameraForm
from apps.camera.models import Camera
from django.urls import reverse_lazy
from django.contrib import messages
from apps.camera.services.rtsp import StreamRTSP


class CameraListView(ListView):
    template_name = "camera/camera.html"
    model = Camera
    context_object_name = "camera"


class CameraCreateView(CreateView):
    template_name = "camera/create_camera.html"
    model = Camera
    form_class = CameraForm
    success_url = reverse_lazy("camera_list")

    def form_valid(self, form):
        messages.success(self.request, "Câmera cadastrada com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar câmera.")
        return super().form_invalid(form)


class CameraUpdateView(UpdateView):
    template_name = "camera/update_camera.html"
    model = Camera
    form_class = CameraForm
    success_url = reverse_lazy("camera_list")

    def form_valid(self, form):
        messages.success(self.request, "Câmera atualizada com sucesso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar câmera.")
        return super().form_invalid(form)


class CameraDeleteView(DeleteView):
    template_name = "camera/delete_camera.html"
    model = Camera
    success_url = reverse_lazy("camera_list")

    def form_valid(self, form):
        camera = self.get_object()
        messages.success(
            self.request, f"Câmera {camera.description} excluída com sucesso."
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["camera"] = self.get_object()
        return context


class StreamView(View):
    def get(self, request, user, password, ip, port):
        return StreamRTSP.video_feed(user, password, ip, port)
