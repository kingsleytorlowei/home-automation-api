from django.db import models

class Room(models.Model):
    sensors = models.ForeignKey(
        'devices.Sensor', related_name='room',
         on_delete=models.CASCADE
         )

    lights = models.ForeignKey(
        'devices.Light',related_name='room',
         on_delete=models.CASCADE
         )

    updated_at = models.DateTimeField(auto_now=True)
    room_name = models.CharField(max_length=100)


    

    class Meta:
        ordering = ['-updated_at']
