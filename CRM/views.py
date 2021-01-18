from rest_framework import generics, viewsets, permissions
from  .models import OrderModel, ServicesModel, ClientsModel
from .serializers import OrderSerializer, ServicesSerializer, ClientsSerializer, CreateOrderSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class OrderView(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        if self.action == 'update':
            return CreateOrderSerializer
        else:
            return OrderSerializer


class ServicesView(viewsets.ModelViewSet):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ClientsView(viewsets.ModelViewSet):
    queryset = ClientsModel.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ClientOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        return OrderModel.objects.filter(order=order_id)
