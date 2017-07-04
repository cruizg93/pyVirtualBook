import datetime
import calendar
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.conf import settings
from easy_pdf.views import PDFTemplateView
from apps.event.models import Event, ItemEvent
from apps.event.forms import EventForm, ItemEventForm

class HelloPDFView(PDFTemplateView):
    template_name = 'reports/contract_PDF.html'
    base_url = 'file://'+settings.STATIC_URL
    download_filename = 'hello.pdf'

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize="A4",
            title='Hi there',
            base_url=self.base_url,
            **kwargs
        )


class ContractPDFView(PDFTemplateView):
    template_name = 'reports/contract_PDF.html'
    base_url = 'file://' + settings.STATIC_URL
    download_filename = 'contract.pdf'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk', 0)
        event = Event.objects.filter(id=pk).first()
        itemEvent = ItemEvent.objects.filter(event__id=pk).first()
        context = super(ContractPDFView, self).get_context_data(
            pagesize="A4",
            title=event.event_name,
            base_url=self.base_url,
            event=event,
            itemEvent=itemEvent,
            **kwargs
        )
        return context


class EventCreate(CreateView):
    model = Event
    second_model = ItemEvent
    template_name = 'event/event_form.html'
    form_class = EventForm
    second_form_class = ItemEventForm
    success_url = reverse_lazy('event:event_list')

    def get_context_data(self, **kwargs):
        context = super(EventCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form1 = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        print(form1.errors)
        print(form2.errors)
        if form1.is_valid() and form2.is_valid():
            itemEvent = form2.save(commit=False)
            itemEvent.event = form1.save()
            itemEvent.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form1=form1, form2=form2))


class CalendarView(ListView):
    model = Event
    template_name = "event/calendar.html"
    actualMonth = datetime.date.today()
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        return arrowed_month(self, context)

    def get_queryset(self):
        new_month = self.request.GET.get("newmonth")
        new_year = self.request.GET.get('newyear')
        if new_month is not None:
            queryset = Event.objects.filter(event_date__month=new_month,
                                            event_date__year=new_year).order_by("event_date")
        else:
            queryset = Event.objects.filter(event_date__month=datetime.date.today().month,
                                            event_date__year=datetime.date.today().year).order_by("event_date")
        response = serializers.serialize("json", queryset)
        return response


class EventList(ListView):
    model = Event
    template_name = 'event/event_list.html'
    actualMonth = datetime.date.today()
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        return arrowed_month(self, context)

    def get_queryset(self):
        new_month = self.request.GET.get("newmonth")
        new_year = self.request.GET.get('newyear')
        if new_month is not None:
            queryset = Event.objects.filter(event_date__month=new_month, event_date__year=new_year).order_by('pk')
        else:
            queryset = Event.objects.filter(event_date__month=datetime.date.today().month,
                                            event_date__year=datetime.date.today().year).order_by('pk')
        return queryset


class EventUpdate(UpdateView):
    model = Event
    second_model = ItemEvent
    template_name = 'event/event_form.html'
    form_class = EventForm
    second_form_class = ItemEventForm
    success_url = reverse_lazy('event:event_list')

    def get_context_data(self, **kwargs):
        context = super(EventUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        event = self.model.objects.get(id=pk)
        itemEvent = self.second_model.objects.filter(event__id=pk).first()
        # sub_total = (itemEvent.quantity*itemEvent.unit_price) + event.delivery_cost
        # event.balance = ((sub_total * (event.tax_percentage/100)) + sub_total)-event.forward_payment
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=itemEvent)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        event = self.model.objects.get(id=id_solicitud)
        itemEvent = self.second_model.objects.get(event__id=id_solicitud)
        form1 = self.form_class(request.POST, instance=event)
        form2 = self.second_form_class(request.POST, instance=itemEvent)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
        return HttpResponseRedirect(self.get_success_url())


class EventDelete(DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy("event:event_list")


# This function determine which is the previous, current & next
# month calendar including year
def arrowed_month(self, context):
    new_month = self.request.GET.get('newmonth')
    year = self.request.GET.get('newyear')
    if new_month is not None:
        if int(new_month) > 12:
            context['month'] = calendar.month_name[1]
            context['previous_month'] = 12
            context['next_month'] = 2
            context['year'] = int(year) + 1
        elif int(new_month) < 1:
            context['month'] = calendar.month_name[12]
            context['previous_month'] = 11
            context['next_month'] = 1
            context['year'] = int(year) - 1
        else:
            context['month'] = calendar.month_name[int(new_month)]
            context['previous_month'] = int(new_month) - 1
            context['next_month'] = int(new_month) + 1
            context['year'] = int(year)
    else:
        context['month'] = calendar.month_name[self.actualMonth.month]
        context['previous_month'] = int(self.actualMonth.month) - 1
        context['next_month'] = int(self.actualMonth.month) + 1
        context['year'] = self.actualMonth.year

    return context
