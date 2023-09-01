from django.contrib import admin
from facturation.models import ReceiptBuy, DeliveryTypes, ReceiptSale, Deliveries

# Register your models here.
admin.site.register(ReceiptBuy)
admin.site.register(DeliveryTypes)
admin.site.register(ReceiptSale)
admin.site.register(Deliveries)