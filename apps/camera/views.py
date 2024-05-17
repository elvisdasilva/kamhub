from django.views.generic import ListView
from apps.camera.models import Camera


class CameraListView(ListView):
    template_name = "camera/camera.html"
    model = Camera
    context_object_name = "camera"
