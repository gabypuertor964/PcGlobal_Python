from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from inventory.models import Products

from .models import Cart
from .utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)
    
    if request.user.is_authenticated:
        # Get the user name
        username = request.user.username
        # Check if the user name exists
        if not username:
            # If the user name does not exist, get the user full name
            fullname = request.user.get_full_name()
    else:
        username = None
        fullname = None
    
    return render(request, 'carts/cart.html',{'cart':cart, 'username': username or fullname})

def add(request):
    cart = get_or_create_cart(request)
    product = Products.objects.get(pk=request.POST.get('product_id'))
    
    if request.user.is_authenticated:
        # Get the user name
        username = request.user.username
        # Check if the user name exists
        if not username:
            # If the user name does not exist, get the user full name
            fullname = request.user.get_full_name()
    else:
        username = None
        fullname = None
    
    cart.products.add(product)
    
    return render(request, 'carts/add.html',{"product": product, 'username': username or fullname})

def remove(request):
    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Products, pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    
    return redirect('cart')