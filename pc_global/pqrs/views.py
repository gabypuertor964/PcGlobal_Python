from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def pqrs(request):
    return render(request, 'my_reports.html')

def CreatePqrs(request):
    return render(request, 'createPqrs.html')

# redenrizacion del index de adminlte3

def adminlte(request):
    return render(request, 'adminlte3.html')