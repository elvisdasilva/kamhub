# Generated by Django 5.0.6 on 2024-05-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0003_alter_camera_ip_alter_camera_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='ip',
            field=models.CharField(max_length=15),
        ),
    ]