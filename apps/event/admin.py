from django.contrib import admin

from apps.event.models import Event, ItemEvent

admin.site.register(Event)
admin.site.register(ItemEvent)
