from django.shortcuts import render
from apps.camera.models import Camera


def home(request):
    return render(request, "home/home.html", {"cameras": Camera.objects.filter(display_on_home=True)})
