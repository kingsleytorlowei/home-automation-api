from django.contrib import admin
from .models import Sensor, Light, Thermostat


#class DeviceAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'device_type', 'location')
#    list_filter = ('device_type', 'location')
class SensorAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'name', 'description', "device_type", "remote_address", "location"]

class LightAdmin(admin.ModelAdmin):
    list_display = ['location', 'status']

class ThermostatAdmin(admin.ModelAdmin):
    list_display = ["mode"]

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
