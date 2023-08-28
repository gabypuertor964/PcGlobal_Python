from django.shortcuts import render
from inventory.models import Productos, Categorias, Marcas

def index(request):
    productos = Productos.objects.all()
    return render(request, 'landing/index.html', {'productos': productos})