from django.contrib import admin
from .models import OrderModel
from .models import ClientsModel
from .models import ServicesModel
# Register your models here.


class OrderInline(admin.TabularInline):
    model = OrderModel
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('order', )


admin.site.register(OrderModel, OrderAdmin)
admin.site.register(ClientsModel)
admin.site.register(ServicesModel)
