from dal import autocomplete
from django import forms
from apps.event.models import Event, ItemEvent
from apps.settings.models import Client, Location, Item


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'location': 'Location',
            'client': 'Client',
            'contact_date': 'Contact Date',
            'drop_off_time': 'Drop Off Time',
            'pick_up_time': 'Pick Up Time',
            'start_time': 'Event Start Time',
            'event_date': 'Event Date',
            'event_name': 'Event Name',
            'comments': 'Comments',
            'forward_payment': 'Forward Payment',
            'tax_percentage':'Tax %',
            'delivery_cost': 'Delivery',
            'state': 'State or Status',
            'ballroom': 'Ballroom Name (If any)',
            'floor_level': 'Floor Level',
        }

        widgets = {
            'location': autocomplete.ModelSelect2(url='settings:location_autocomplete', attrs={'class': 'form-control'}),
            'client': autocomplete.ModelSelect2(url='settings:client_autocomplete', attrs={'class': 'form-control'}),
            'contact_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'drop_off_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time', 'class':	'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class':	'form-control'}),
            'comments': forms.Textarea(attrs={'class':	'form-control, commentField'}),
            'forward_payment': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'tax_percentage': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'delivery_cost': forms.TextInput(attrs={'class':	'form-control calculateTotal'}),
            'state': forms.TextInput(attrs={'class':	'form-control'}),
            'ballroom': forms.TextInput(attrs={'class': 'form-control'}),
            'floor_level': forms.TextInput(attrs={'class': 'form-control'}),
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
            'item': autocomplete.ModelSelect2(url='settings:item_autocomplete',attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':	'form-control calculateTotal'}),
            'unit_price': forms.NumberInput(attrs={'class':	'form-control calculateTotal', 'step': 0.25}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemEventForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.order_by('description')
