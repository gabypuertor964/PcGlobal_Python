from django.shortcuts import render
from inventory.models import Products, Categories

def index(request):
    return render(request, 'landing/index.html')

def categorias(request, categoria):
    categoria_result = Categories.objects.get(slug=categoria)
    productos = Products.objects.filter(categoria__slug=categoria_result.slug)
    return render(request, 'landing/products/categories.html',{"categoria": categoria_result, "productos": productos})