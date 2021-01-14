from django.urls import path
from .views import OrderView, ServicesView, ClientsView

urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('services/', ServicesView.as_view()),
    path('clients/', ClientsView.as_view()),
]
