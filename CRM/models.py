from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save, post_init, pre_init
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class ClientsModel(models.Model):
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{0}'.format(self.client_name)


class ServicesModel(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{0} {1}".format(self.service_name, self.price)


class OrderModel(models.Model):
    choices = [
        ('Поступил(а', 'Поступил(а)'),
        ('Согласован', 'Согласовано'),
        ('Отказ', 'Отказ'),
        ('Ожидает запчаст', 'Ожидает запчасти'),
        ('В процесс', 'В процессе'),
        ("Готов", "Готов"),
        ("Не оплачен", 'Не оплачен'),
        ("Оплачен", 'Оплачен')]
    _client = models.ForeignKey(
        ClientsModel, on_delete=models.PROTECT, blank=True)
    order = models.ManyToManyField(ServicesModel, related_name="services")
    clients = models.ManyToManyField(ClientsModel, related_name='clients', blank=True)
    executioner = models.ForeignKey(
        User, related_name="executioner", on_delete=models.PROTECT)
    _price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(choices=choices, max_length=100)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.client, self.order_date)

    @property
    def price(self):
        total_cost = 0
        for order in self.order.all():
            total_cost += order.price
        return total_cost

    @price.setter
    def price(self, value):
        print(value)
        self._price = value
        
    @property
    def client(self):
        clients_data = ClientsModel.objects.filter(client_name=self._client).first()
        return '{} {}'.format(clients_data.client_name, clients_data.address)

    @client.setter
    def client(self, value):
        print(value)
        self._client = value

@receiver(post_init, sender=OrderModel)
def set_price_value(sender, instance, *args, **kwargs):
    instance._price = instance.price