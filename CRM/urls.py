from django.urls import path, include
from .views import (OrderView, ServicesView, ClientsView,
                    ClientOrderView, create_environment)

urlpatterns = [
    path('orders/', OrderView.as_view({'get': 'list', 'post': 'create'})),
    path('orders/<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('orders/client/<int:pk>/', ClientOrderView.as_view()),
    path('services/', ServicesView.as_view({'get': 'list'})),
    path('services/create/', ServicesView.as_view({'post': 'create'})),
    path('services/<int:pk>/', ServicesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('clients/', ClientsView.as_view({'get': 'list'})),
    path('clients/create/', ClientsView.as_view({'post': 'create'})),
    path('clients/<int:pk>/', ClientsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('environment/', create_environment, name='create_environment')
]
