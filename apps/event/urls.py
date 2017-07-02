from django.conf.urls import url, include
from apps.event.views import EventCreate, EventList, EventUpdate, EventDelete
from apps.event.views import CalendarView, ContractPDFView
urlpatterns = [
    url(r'^$',CalendarView.as_view(),name='calendarView'),
    url(r'^myCalendar$',CalendarView.as_view(),name='calendarView'),
    url(r'^myCalendar/(?P<newmonth>\w+)$',CalendarView.as_view(),name='calendarView'),
    url(r'^index$',EventList.as_view(),name='event_list'),
    url(r'^create$',EventCreate.as_view(),name='event_create'),
    url(r'^listing$',EventList.as_view(),name='event_list'),
    url(r'^listing/(?P<newmonth>\w+)$',EventList.as_view(),name='event_list'),
    url(r'^edit/(?P<pk>\d+)$',EventUpdate.as_view(),name='event_update'),
    url(r'^delete/(?P<pk>\d+)$',EventDelete.as_view(),name='event_delete'),
    url(r'^contract.pdf$', ContractPDFView.as_view(), name="pdf")
]
