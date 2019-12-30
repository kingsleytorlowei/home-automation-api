from django.db import models


class House(models.Model):
    """
    House model for adding rooms, controlling the thermostat 
    """
    OFF = "OFF"
    COOL = "COOL"
    HEAT ="HEAT"
    FAN_ON = "FAN-ON"
    AUTO = "AUTO"

    #Thermostat modes
    MODES = (
    (OFF, 'off'),
    (COOL, 'cool'),
    (HEAT,'heat' ),
    (FAN_ON, 'fan-on'),
    (AUTO, 'auto')
    )

    rooms = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
