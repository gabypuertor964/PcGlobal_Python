import uuid
import decimal
from django.db import models
from authentication.models import UserCustom
from inventory.models import Products
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(
        UserCustom,
        null=True,
        blank=True,
        on_delete=models.CASCADE,)
    
    products = models.ManyToManyField(Products)
    
    subtotal = models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=2)
    
    total = models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    FEE = 0.05
    
    def __str__(self):
        return self.cart_id
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
    
    def update_subtotal(self):
        self.subtotal = sum([ product.precio for product in self.products.all() ])
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()
    
    class Meta:
        verbose_name = 'Carrito de compras'
        verbose_name_plural = 'Carritos de compras'
        
        db_table = 'carrito_de_compras'
        ordering = ['id']
        
def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())
        
def update_totals(sender, instance, action, *args, **kwargss):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_cart_id, sender=Cart)
m2m_changed.connect(update_totals, sender=Cart.products.through)