#Default Django Imports
from django.contrib import admin
from django.urls import path

# Import Auth Views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # View: Login
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
]
