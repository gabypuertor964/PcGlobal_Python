from django.shortcuts import render
from inventory.models import Products, Categories
from django.core.paginator import Paginator
from django.http import Http404
import markdown

def index(request):
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

    # Render the template with its context
    return render(request, 'index.html', {'username': username or fullname})

def categories(request, category_name):

    try:
        # Get the category object
        category = Categories.objects.get(slug=category_name)

    # If we can't find the category, raise an HTTP 404 error
    except Categories.DoesNotExist:
        raise Http404("La categoria no existe")

    # Get the products for the category
    products = Products.objects.filter(categoria__slug=category.slug)
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(products, 12)
        products = paginator.page(page)
    except:
        raise Http404("La categoria no existe")

    # Render the page
    return render(request, 'products/categories.html',{"category": category, "entity": products, "paginator": paginator,})

def product_view(request, product_name):
    
    try:
        product = Products.objects.get(slug=product_name)
    except Products.DoesNotExist:
        raise Http404("El producto no existe")
        
    descripcion_1_md = markdown.markdown(product.descripcion_1)
    descripcion_2_md = markdown.markdown(product.descripcion_2)
    
    return render(request, 'products/product.html', {"producto": product, 'descripcion_1_md': descripcion_1_md, "descripcion_2_md": descripcion_2_md})

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


