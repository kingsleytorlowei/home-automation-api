from django.contrib import admin
from .models import Sensor, Light, Thermostat


#class DeviceAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'device_type', 'location')
#    list_filter = ('device_type', 'location')
class SensorAdmin(admin.ModelAdmin):
    
    list_display = [
            'created_at', 'updated_at',
            'name', 'description', "device_type",
            "remote_address"
            ]




class LightAdmin(admin.ModelAdmin):
    list_display = [
            'is_on', "created_at",
            "updated_at"
            ]




class ThermostatAdmin(admin.ModelAdmin):
    list_display = [
            "mode", "created_at",
            "updated_at"
            ]




admin.site.register(Sensor, SensorAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
