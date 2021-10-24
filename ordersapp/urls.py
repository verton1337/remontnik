from django.conf.urls import url
from django.urls import path
import ordersapp.views as ordersapp
from django.contrib.auth.decorators import login_required

from ordersapp.views import OrderAPI
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path("", ordersapp.CreateOrderView.as_view(), name="new_order"),
    path("list/", login_required(ordersapp.ListOrdersView.as_view()), name="orders_list"),
    path("assign_to_me/<int:pk>", login_required(ordersapp.AsignView.as_view()), name="assign_ticket_to_me"),
    path("details/<int:pk>", login_required(ordersapp.OrderDetailView.as_view()), name="order_details"),
    path("my_orders/", login_required(ordersapp.WorkerOrdersView.as_view()), name="worker_orders"),

    
]
router = DefaultRouter()
router.register(r'api', OrderAPI, basename='user')
urlpatterns += router.urls
