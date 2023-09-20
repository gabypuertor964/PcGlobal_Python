from django.contrib import admin
from django.urls import path
from . import views
from .views import PqrsListView, PqrsUpdateView
# from django.urls import include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('reports/', PqrsListView.as_view(), name='reports'),
    path('createpqrs/', views.CreatePqrs, name='create-pqrs'),
    path('updatepqrs/<int:pk>', PqrsUpdateView.as_view(), name='update-pqrs'),
    path('delete-pqrs/<int:id>',views.delete_pqrs, name='delete-pqrs')
]