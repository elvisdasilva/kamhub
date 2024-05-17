from django.db import models
from apps.environment.models import CameraEnvironment


class Camera(models.Model):
    description = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(protocol="both", unpack_ipv4=True, unique=True)
    port = models.IntegerField()
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    display_on_home = models.BooleanField(default=False)
    camera_environment = models.ForeignKey(
        CameraEnvironment,
        on_delete=models.CASCADE,
        related_name="camera_environment",
        verbose_name="Camera environment",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
