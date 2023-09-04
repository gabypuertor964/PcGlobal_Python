from django.shortcuts import render
from inventory.models import Products, Categories
#from django.http import Http404
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def categories(request, category_name):

    try:
        # Get the category object
        category = Categories.objects.get(slug=category_name)

    # If we can't find the category, raise an HTTP 404 error
    except Categories.DoesNotExist:
        return HttpResponse("Categoria no encontrada")

    # Get the products for the category
    products = Products.objects.filter(categoria__slug="tarjetas-graficas").select_related('marca')

    # Render the page
    return render(request, 'categories.html',{"category": category, "products": products})