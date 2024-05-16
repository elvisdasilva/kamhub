from django.forms import ModelForm
from apps.environment.models import CameraEnvironment


class CameraEnvironmentForm(ModelForm):
    class Meta:
        model = CameraEnvironment
        fields = "__all__"
