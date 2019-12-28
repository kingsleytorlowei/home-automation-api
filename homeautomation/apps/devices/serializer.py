from .models import Device
from rest_framework import serializers

#class DeviceSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Device
#        fields = ("id","name",  "created_at", "updated_at", "description", "device_type", "remote_address", "location")