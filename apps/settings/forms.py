from django import forms

from apps.settings.models import Item, Client, Location


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'description',
            'quantity',
            'state',
        ]
        labels = {
            'description': 'Description',
            'quantity': 'Quantity',
            'state': 'State',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class':	'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'phone_number',
            'email',
            'company_name',
            'billing_address',
        ]
        labels = {
            'name': 'Name',
            'phone_number': 'Phone Number',
            'email': 'E-mail',
            'company_name': 'Company Name',
            'billing_address': 'Billing Address',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':	'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':	'form-control appUSPhoneNumber'}),
            'email': forms.TextInput(attrs={'class': 'form-control appEmail'}),
            'company_name': forms.TextInput(attrs={'class':	'form-control'}),
            'billing_address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'address',
            'state',
            'county',
            'city',
            'zipcode',
            'building_name',
            'phone_number',
        ]
        labels = {
            'address': 'Address',
            'city': 'City',
            'county': 'County',
            'state': 'State',
            'zipcode': 'ZipCode',
            'building_name': 'Building Name',
            'phone_number': 'Phone Number',
        }
        widgets = {
            'address': forms.TextInput(attrs={'class':	'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'county': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':	'form-control appUSPhoneNumber'}),
        }