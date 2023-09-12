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

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
