from django.db import models

from apps.settings.models import Location, Client, Item


class Event(models.Model):

    location = models.ForeignKey(Location, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    contact_date = models.DateField(null=True, blank=True)
    drop_off_time = models.TimeField(null=True, blank=True)
    pick_up_time = models.TimeField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_name = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)
    forward_payment = models.FloatField(null=True, blank=True, default=0)
    tax_percentage = models.FloatField(null=True, blank=True, default=0)
    delivery_cost = models.FloatField(null=True, blank=True, default=0)
    state = models.PositiveSmallIntegerField(null=True, blank=True,default=1)
    ballroom = models.CharField(null=True, blank=True, max_length=100)
    floor_level = models.CharField(null=True, blank=True, max_length=100)
    balance = 0

    def __str__(self):
        return '{} | {}{}'.format(self.event_date, self.client.name, self.client.company_name)


class ItemEvent(models.Model):
    event = models.ForeignKey(Event,null=True, blank=True)
    item = models.ForeignKey(Item,null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.item.description, self.event.event_name)
