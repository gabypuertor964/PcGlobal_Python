from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'principal/index.html')

def saludo(request):
    return render(request, 'landing_page/home.html')