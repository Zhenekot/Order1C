from django.contrib import admin
from .models import Product,Car, Order,PlaceFrom,PlaceImpl,Client
# Register your models here.


admin.site.register(Product)
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(PlaceImpl)
admin.site.register(PlaceFrom)
admin.site.register(Order)