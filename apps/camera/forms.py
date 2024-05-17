from django.forms import ModelForm
from apps.camera.models import Camera


class CameraForm(ModelForm):
    class Meta:
        model = Camera
        fields = "__all__"
