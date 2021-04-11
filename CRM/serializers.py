from rest_framework import serializers
from .models import OrderModel, ServicesModel, ClientsModel


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsModel
        fields = ['client_name', 'phone_number', 'address']


class OrderSerializer(serializers.ModelSerializer):
    executioner = serializers.ReadOnlyField(source='executioner.username')
    # client = serializers.ReadOnlyField(source='client.client_name')
    order = ServicesSerializer(read_only=True, many=True)
    # clients = serializers.ReadOnlyField(source='clients.client_name')D
    clients = ClientsSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        # fields = '__all__'
        fields = ['executioner', 'client', 'order',
                  'status', 'order_date', 'price', 'clients']


class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel
        fields = ['executioner', 'client', 'order',
                  'status', 'order_date', 'total_price']
