from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from inventory.models import Products

from .models import Cart
from .utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)
    
    return render(request, 'carts/cart.html',{'cart':cart})

def add(request):
    cart = get_or_create_cart(request)
    product = Products.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(product)
    
    return render(request, 'carts/add.html',{"product": product})

def remove(request):
    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Products, pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    
    return redirect('cart')