from django import forms
from django.forms import extras
from apps.event.models import Event, ItemEvent


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = {
            'location',
            'client',
            'contact_date',
            'drop_off_time',
            'pick_up_time',
            'event_date',
            'event_name',
            'comments',
            'forward_payment',
            'tax_percentage',
            'delivery_cost',
            'state',
        }
        labels = {
            'location': 'Location',
            'client': 'Client',
            'contact_date': 'Contact Date',
            'drop_off_time': 'Drop Off Time',
            'pick_up_time': 'Pick Up Time',
            'event_date': 'Event Date',
            'event_name': 'Event Name',
            'comments': 'Comments',
            'forward_payment': 'Forward Payment',
            'tax_percentage':'Tax %',
            'delivery_cost': 'Delivery',
            'state': 'State or Status',
        }
        widgets = {
            'location': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'contact_date': forms.DateInput(attrs={'class':	'form-control'}),
            'drop_off_time': forms.TimeInput(attrs={'class':	'form-control'}),
            'pick_up_time': forms.TimeInput(attrs={'class':	'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class':	'form-control'}),
            'comments': forms.Textarea(attrs={'class':	'form-control, commentField'}),
            'forward_payment': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'tax_percentage': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'delivery_cost': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'state': forms.TextInput(attrs={'class':	'form-control'}),
        }


class ItemEventForm(forms.ModelForm):
    class Meta:
        model = ItemEvent
        fields = [
            'item',
            'quantity',
            'unit_price',
        ]
        labels = {
            'item': 'Item ',
            'quantity': 'Quantity',
            'unit_price': 'Unit Price',
        }
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':	'form-control calculateTotal'}),
            'unit_price': forms.NumberInput(attrs={'class':	'form-control calculateTotal', 'step': 0.25}),
        }