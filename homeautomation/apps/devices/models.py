from django.db import models


class Sensor(models.Model):
    """
    The Sensor model 
    """
    TEMPERATURE = "TEMPERATURE SENSOR"

    DEVICE_TYPES = (
        (TEMPERATURE, "Temperature Sensor"),
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    device_type = models.CharField(max_length=100, choices=DEVICE_TYPES)
    remote_address = models.CharField(('IP Address'), max_length=255)
#    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, blank=True, null=True)

class Light(models.Model):
    """
    The Light Model
    """
#    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    is_on = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Thermostat(models.Model):
    """
    The thermostat model
    """
    #Different modes of the thermostat
    OFF = "OFF"
    COOL = "COOL"
    HEAT = "HEAT"
    FAN_ON = "FAN-ON"
    AUTO = "AUTO"

    MODES = (
        (OFF, "OFF"),
        (COOL, "COOL"),
        (HEAT, "HEAT"),
        (FAN_ON, "FAN-ON"),
        (AUTO, "AUTO")
    )

    mode = models.CharField(max_length=50,choices=MODES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)