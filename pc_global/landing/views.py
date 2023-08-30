from django.shortcuts import render
from inventory.models import Productos, Categorias

def index(request):
    return render(request, 'landing/index.html')

def categorias(request, categoria):
    categoria_result = Categorias.objects.get(slug=categoria)
    productos = Productos.objects.filter(categoria__slug=categoria_result.slug)
    return render(request, 'productos/categorias.html',{"categoria": categoria_result, "productos": productos})