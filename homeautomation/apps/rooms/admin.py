from django.contrib import admin
from homeautomation.apps.rooms.models import Room


#class RoomAdmin(admin.ModelAdmin):
 #   list_display = ("id","devices","updated_at")


admin.site.register(Room)