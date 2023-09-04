from django.shortcuts import render
from inventory.models import Products, Categories
from django.http import Http404

def index(request):
    return render(request, 'index.html')

def categories(request, category_name):

    try:
        # Get the category object
        category = Categories.objects.get(slug=category_name)

    # If we can't find the category, raise an HTTP 404 error
    except Categories.DoesNotExist:
        raise Http404("La categoria no existe")

    # Get the products for the category
    products = Products.objects.filter(categoria__slug="tarjetas-graficas").select_related('marca')

    # Render the page
    return render(request, 'products/categories.html',{"category": category, "products": products})

# Error: Not Found
def handler404(request, exception):

    # Get the exception message
    context = {
        'exception': exception
    }

    # Render the page
    return render(request, 'errors/404.html', context, status=404)

# Error: Internal Server Error
def handler500(request):
    return render(request, 'errors/500.html', status=500)

# Error: Forbidden
def handler403(request, exception):
    return render(request, 'errors/403.html', status=403)

# Error: Bad Request
def handler400(request, exception):
    return render(request, 'errors/400.html', status=400)

# Error: Unauthorized
def handler401(request, exception):
    return render(request, 'errors/401.html', status=401)

# Error: MRequest Timeout
def handler408(request, exception):
    return render(request, 'errors/408.html', status=405)


