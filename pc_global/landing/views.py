from django.shortcuts import render
from inventory.models import products, categories

def index(request):
    return render(request, 'landing/index.html')

def categorias(request, categoria):
    categoria_result = categories.objects.get(slug=categoria)
    productos = products.objects.filter(categoria__slug=categoria_result.slug)
    return render(request, 'productos/categorias.html',{"categoria": categoria_result, "productos": productos})