from django.urls import path
from . import views

urlpatterns = [

    # Display Home Page
    path('', views.index, name='index'),

    # Display products for a given data category
    path('categorias/<category_name>/', views.categories, name='categorias')
]
