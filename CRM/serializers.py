from rest_framework import serializers
from .models import OrderModel, ServicesModel, ClientsModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsModel
        fields = '__all__'
