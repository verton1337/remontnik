from django.forms import fields
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from ordersapp.forms import OrderForm, UpdateOrderForm
from ordersapp.models import Order
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework import viewsets

# Create your views here.

class CreateOrderView(CreateView):
    template_name = "ordersapp/index.html"
    model = Order
    fields = ['userName', 'phone']
    success_url = reverse_lazy("main:mainpage")

    def get_context_data(self, **kwargs):
        data =  super(CreateOrderView, self).get_context_data(**kwargs)

        if self.request.POST:
            form = OrderForm(self.request.POST)
            if form.is_valid:
                form.save()
        else:
            form = OrderForm()
        
        data["orderform"] = form
        return data


class ListOrdersView(ListView):
    template_name = "ordersapp/orders_list.html"
    model = Order
    def  get_queryset(self):
        return Order.objects.all().select_related().exclude(status__in = ("CNC", "RDY"))

    def get_context_data(self, **kwargs):
        data = super(ListOrdersView, self).get_context_data(**kwargs)

        data["unformed_orders"] = len(Order.objects.filter(status="FM"))
        print(data["unformed_orders"])
        return data


class AsignView(TemplateView):
    template_name = "ordersapp/base.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        data =  super(AsignView, self).get_context_data(**kwargs)
        order = get_object_or_404(Order, pk=pk)
        order.worker = self.request.user
        order.status = "STP"
        order.save()
        HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return data


class OrderDetailView(UpdateView):
    template_name = "ordersapp/details.html"
    model = Order
    fields = "__all__"
    success_url = reverse_lazy("order:orders_list")


    

    def get_context_data(self, **kwargs):

        data = super(OrderDetailView, self).get_context_data(**kwargs)
        if self.request.POST:
            form = UpdateOrderForm(self.request.POST, instance=self.object)
            form.save()
        else:
            form = UpdateOrderForm(instance=self.object)


        data["form"] = form
       
        return data


class WorkerOrdersView(ListView):

    template_name = "ordersapp/orders_list.html"
    model = Order

    def  get_queryset(self):
        return Order.objects.filter(worker=self.request.user.pk).select_related().exclude(status__in = ("CNC", "RDY"))


class OrderAPI(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def put(self, request, *args, **kwargs):
        item = Order.objects.create(userName = request.data['userName'], phone = request.data['phone'])
        item.save()
        return Response({'msg':'ok', 'status':200})


    

    
