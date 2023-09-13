from django.contrib import admin
from django.urls import path
from . import views
# from django.urls import include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('reports/', views.pqrs, name='reports'),
    path('createpqrs/', views.CreatePqrs, name='create-pqrs'),
]