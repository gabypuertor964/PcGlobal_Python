from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from inventory.models import Products, Categories

def index(request):
    return render(request, 'landing/index.html')

def categorias(request, categoria):
    categoria_result = Categories.objects.get(slug=categoria)
    productos = Products.objects.filter(categoria__slug=categoria_result.slug)
    return render(request, 'landing/products/categories.html',{"categoria": categoria_result, "productos": productos})


def login_view(request):
        if request.method == 'POST':
            input_username = request.POST.get('username')
            input_password = request.POST.get('password')

            user = authenticate(username=input_username, password=input_password)
            if user:
                login(request, user)
                messages.success(request, 'Bienvenido {}'.format(user.username))
                return redirect('admin:index')
            else: 
                messages.error(request, 'Usuario o contraseña incorrectos')

        return render(request, 'landing/login/login.html')