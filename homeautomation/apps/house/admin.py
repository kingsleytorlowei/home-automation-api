from django.contrib import admin
from homeautomation.apps.house.models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ("id","rooms")


admin.site.register(House, HouseAdmin)