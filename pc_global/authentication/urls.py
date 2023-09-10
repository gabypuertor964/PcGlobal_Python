#Default Django Imports
from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView

# Import Auth Views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Route GET/POST: Login
    path('login/', LoginView.as_view(), name='login'),

    # Route GET/POST: Register
    path('register/', RegisterView.as_view(), name='register'),
]
