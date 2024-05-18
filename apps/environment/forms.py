from django import forms
from apps.environment.models import CameraEnvironment


class CameraEnvironmentForm(forms.ModelForm):

    class Meta:
        model = CameraEnvironment
        widgets = {
            "description": forms.TextInput(
                attrs={"class": "form-control form-control-user", "placeholder": "ex: sala de estar"}
            )
        }
        fields = "__all__"
