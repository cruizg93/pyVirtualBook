from django.contrib import admin

from django.contrib import admin

from apps.settings.models import Location, Client, Item

admin.site.register(Location)
admin.site.register(Item)
admin.site.register(Client)