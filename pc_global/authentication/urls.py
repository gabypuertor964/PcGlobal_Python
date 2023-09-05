#Default Django Imports
from django.contrib import admin
from django.urls import path
from .views import RegisterView

# Import Auth Views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # View: Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
