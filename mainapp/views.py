from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from ordersapp.models import Order
from ordersapp.forms import OrderForm
# Create your views here.


class MainView(TemplateView):
    template_name = "mainapp/index.html"


class ContactsView(CreateView):
    template_name = "mainapp/contacts.html"

    model = Order
    fields = ['userName', 'phone']
    success_url = reverse_lazy("main:mainpage")

    def get_context_data(self, **kwargs):
        data =  super(ContactsView, self).get_context_data(**kwargs)

        if self.request.POST:
            form = OrderForm(self.request.POST)
            if form.is_valid:
                form.save()
        else:
            form = OrderForm()
        
        data["form"] = form
        return data

class WorksView(TemplateView):
    template_name = "mainapp/work.html"
