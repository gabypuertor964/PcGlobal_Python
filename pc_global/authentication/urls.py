#Default Django Imports
from django.contrib import admin
from django.urls import path
from .views import RegisterView

# Import Auth Views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Route GET/POST: Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Route GET/POST: Register
    path('register/', RegisterView.as_view(), name='register'),
]
