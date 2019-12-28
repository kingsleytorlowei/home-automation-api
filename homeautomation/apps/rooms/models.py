from django.db import models

class Room(models.Model):
    sensors = models.ForeignKey('devices.Sensor', related_name='room', on_delete=models.CASCADE)
  #  lights = models.ForeignKey('lights.Light', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
