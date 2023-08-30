from django.contrib import admin
from facturation.models import receiptBuy, deliveryTypes, receiptSale, deliveries

# Register your models here.
admin.site.register(receiptBuy)
admin.site.register(deliveryTypes)
admin.site.register(receiptSale)
admin.site.register(deliveries)