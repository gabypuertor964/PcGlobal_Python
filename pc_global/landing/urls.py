from django.urls import path,include
from . import views

urlpatterns = [
    # Display Home Page
    path('', views.index, name='index'),

    # Display products for a given data category
    path('categorias/<category_name>/', views.categories, name='categorias'),
    path('productos/<product_name>/', views.product_view, name='productos'),

    # Display the dashboard and Utilities (Client)
    path('client/', views.dashboard, name='dashboard_client'),
    path('client/pqrs/',include('pqrs.urls')),
    path('client/facturation/',include('facturation.urls')),

    # Display the dashboard and Utilities (Workers)
    path('workers/', views.dashboard, name='dashboard_workers'),
    path('workers/inventory/',include('inventory.urls')),
    path('workers/facturation/',include('facturation.urls')),
    path('workers/pqrs/',include('pqrs.urls')),
]
