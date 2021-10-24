from rest_framework import serializers
from ordersapp.models import Order
class OrderSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(max_length=64)
    phone = serializers.CharField(max_length=20)
 
    class Meta:
        model = Order
        fields = ['userName', 'phone', 'status']