from django.conf.urls import url, include
from apps.settings.views import ClientCreate,ClientList, ClientUpdate, ClientDelete, ClientAutocomplete
from apps.settings.views import LocationCreate, LocationList, LocationUpdate, LocationDelete, LocationAutocomplete
from apps.settings.views import ItemCreate, ItemList, ItemUpdate, ItemDelete, ItemAutocomplete
from apps.settings.views import settings_menu

urlpatterns = [
    url(r'^$', settings_menu, name="settingsMenu"),
    url(r'^client-autocomplete/$', ClientAutocomplete.as_view(), name='client_autocomplete'),
    url(r'^location-autocomplete/$', LocationAutocomplete.as_view(), name='location_autocomplete'),
    url(r'^item-autocomplete/$', ItemAutocomplete.as_view(), name='item_autocomplete'),
    url(r'^client/create$', ClientCreate.as_view(), name='client_create'),
    url(r'^client/create/(?P<modal>\d+)/$', ClientCreate.as_view(), name='client_create'),
    url(r'^client$', ClientList.as_view(), name='client_list'),
    url(r'^client/list$', ClientList.as_view(), name='client_list'),
    url(r'^client/update/(?P<pk>\d+)/$', ClientUpdate.as_view(), name='client_update'),
    url(r'^client/delete/(?P<pk>\d+)/$', ClientDelete.as_view(), name='client_delete'),
    url(r'^location/create$', LocationCreate.as_view(), name='location_create'),
    url(r'^location$', LocationList.as_view(), name='location_list'),
    url(r'^location/list', LocationList.as_view(), name='location_list'),
    url(r'^location/update/(?P<pk>\d+)/$', LocationUpdate.as_view(), name='location_update'),
    url(r'^location/delete/(?P<pk>\d+)/$', LocationDelete.as_view(), name='location_delete'),
    url(r'^item/create$', ItemCreate.as_view(), name="item_create"),
    url(r'^item$', ItemList.as_view(), name="item_list"),
    url(r'^item/list$', ItemList.as_view(), name="item_list"),
    url(r'^item/update/(?P<pk>\d+)/$', ItemUpdate.as_view(), name='item_update'),
    url(r'^item/delete/(?P<pk>\d+)/$', ItemDelete.as_view(), name='item_delete'),
]
