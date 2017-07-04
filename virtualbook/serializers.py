from apps.event.models import Event
from apps.settings.models import Location, Client, Item
from rest_framework import serializers


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):
    client = ClientSerializers()
    location = Location()
    class Meta:
        path = 1
        model = Event
        fields = '__all__'
