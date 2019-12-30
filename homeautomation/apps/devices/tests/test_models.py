from django.test import TestCase
from homeautomation.apps.devices.models import Sensor, Light, Thermostat


class TestSensor(TestCase):
    def setUp(self):
        self.sensor = Sensor.objects.create(name='TP-LINK',
                                            description='Sensor that reads temperature',
                                            device_type='Temperature Sensor',
                                            remote_address="1.0.0.1",
                                            )

    def test_dates(self):
        self.assertGreater(self.sensor.updated_at,
                           self.sensor.created_at)

    def test_str(self):
        self.assertEqual(str(self.sensor), self.sensor.name)
