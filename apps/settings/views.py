from django.shortcuts import render
from apps.settings.models import Client, Location, Item
from apps.settings.forms import ClientForm, LocationForm, ItemForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


def index(request):
    return render(request, "base/welcome.html")


def settings_menu(request):
    return render(request, "settings/settings_menu.html")


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'settings/client_form.html'
    success_url = reverse_lazy('event:event_list')


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'settings/client_form.html'
    success_url = reverse_lazy('settings:client_list')


class ClientList(ListView):
    model = Client
    template_name = 'settings/client_list.html'
    paginate_by = 10
    ordering = ['company_name']


class ClientDelete(DeleteView):
    model = Client
    template_name = 'settings/client_delete.html'
    success_url = reverse_lazy('settings:client_list')


class LocationCreate(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'settings/location_form.html'
    success_url = reverse_lazy('settings:location_list')


class LocationUpdate(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'settings/location_form.html'
    success_url = reverse_lazy('settings:location_list')


class LocationList(ListView):
    model = Location
    template_name = 'settings/location_list.html'
    paginate_by = 10
    ordering = ['building_name']


class LocationDelete(DeleteView):
    model = Location
    template_name = 'settings/location_delete.html'
    success_url = reverse_lazy('settings:location_list')


class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'settings/item_form.html'
    success_url = reverse_lazy('settings:item_list')


class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'settings/item_form.html'
    success_url = reverse_lazy('settings:item_list')


class ItemList(ListView):
    model = Item
    template_name = 'settings/item_list.html'
    paginate_by = 10
    ordering = ['description']


class ItemDelete(DeleteView):
    model = Item
    template_name = 'settings/item_delete.html'
    success_url = reverse_lazy('settings:item_list')