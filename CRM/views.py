from django.shortcuts import render
from rest_framework import generics
from  .models import OrderModel, ServicesModel, ClientsModel
from .serializers import OrderSerializer, ServicesSerializer, ClientsSerializer


# Create your views here.
class OrderView(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class ServicesView(generics.ListAPIView):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer


class ClientsView(generics.ListAPIView):
    queryset = ClientsModel.objects.all()
    serializer_class = ClientsSerializer
