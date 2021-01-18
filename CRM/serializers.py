from rest_framework import serializers
from .models import OrderModel, ServicesModel, ClientsModel


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsModel
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    executioner = serializers.ReadOnlyField(source='executioner.username')
    client = serializers.ReadOnlyField(source='client.client_name')
    order = ServicesSerializer(read_only=True, many=True)

    class Meta:
        model = OrderModel
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel
        fields = '__all__'
