from django.db import models


class House(models.Model):
    #Thermostat modes
    MODES = (
    ('off', 'off'),
    ('cool', 'cool'),
    ('heat','heat' ),
    ('fan-on', 'fan-on'),
    ('auto', 'auto')
    )

    owner = models.CharField(max_length=50)
    rooms = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    thermostat = models.CharField(choices=MODES)