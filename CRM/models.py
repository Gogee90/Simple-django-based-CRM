from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ClientsModel(models.Model):
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.client_name


class ServicesModel(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{0} {1}".format(self.service_name, self.price)


class OrderModel(models.Model):
    choices = [
      ('Arrived', 'Поступил(а)'),
      ('Confirmed', 'Согласовано'),
      ('Declined', 'Отказ'),
      ('Awaiting', 'Ожидает запчасти'),
      ('Work in progress', 'В процессе'),
      ("Job's done", "Готов"),
      ("Not_paid", 'Не оплачен'),
      ("Paid", 'Оплачен')]
    client = models.ForeignKey(ClientsModel, related_name="clients", on_delete=models.PROTECT, blank=True)
    order = models.ManyToManyField(ServicesModel, related_name="services")
    executioner = models.ForeignKey(User, related_name="executioner", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(choices=choices, max_length=100)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{0} {1}".format(self.client, self.order_date)
