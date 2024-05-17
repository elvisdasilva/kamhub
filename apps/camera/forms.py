from django import forms
from apps.camera.models import Camera


class CameraForm(forms.ModelForm):

    class Meta:
        model = Camera
        widgets = {
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ex: frente rua lado esquerdo"}
            ),
            "ip": forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: 192.168.1.2"}),
            "port": forms.NumberInput(attrs={"class": "form-control", "placeholder": "ex: 554"}),
            "user": forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: admin"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "ex: 123"}),
            "display_on_home": forms.CheckboxInput(
                attrs={"class": "form-check-input custom-control-input"}
            ),
            "camera_environment": forms.Select(
                attrs={"class": "form-select select2bs4 form-control"}
            ),
        }
        fields = "__all__"
