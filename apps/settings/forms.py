from django import forms

from apps.settings.models import Item, Client, Location

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields=[
			'description',
			'quantity',
			'state',
		]
		labels = {
			'description':'Description',
			'quantity' :'Quantity',
			'state': 'State',
		}
		widgets = {
			'description':forms.TextInput(attrs={'class':	'form-control'}),
			'quantity':forms.TextInput(attrs={'class':	'form-control'}),
			'state':forms.TextInput(attrs={'class':	'form-control'}),
		}

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = [
			'name',
			'phone_number',
			'email',
			'company_name',
		]
		labels = {
			'name':'Name',
			'phone_number':'Phone Number',
			'email':'E-mail',
			'company_name':'Company Name',
		}
		widgets = {
			'name':forms.TextInput(attrs={'class':	'form-control'}),
			'phone_number':forms.TextInput(attrs={'class':	'form-control'}),
			'email':forms.TextInput(attrs={'class':	'form-control'}),
			'company_name':forms.TextInput(attrs={'class':	'form-control'}),
		}

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = [
			'location',
			'building_name',
			'phone_number',
		]
		labels = {
			'location' : 'Location',
			'building_name':'Building Name',
			'phone_number' : 'Phone Number',
		}
		widgets = {
			'location':forms.TextInput(attrs={'class':	'form-control'}),
			'building_name':forms.TextInput(attrs={'class':	'form-control'}),
			'phone_number':forms.TextInput(attrs={'class':	'form-control'}),
		}