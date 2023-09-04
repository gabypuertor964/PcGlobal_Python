#Default Django Imports
from django.contrib import admin
from django.urls import path

from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Landing Page URLs
    path('',include('landing.urls')),

    # Authentication URLs
    path('auth/', include('authentication.urls')),

    # Admin Panel Url
    path('admin/', admin.site.urls, name='admin:index'),
]

# Static and Media URLs (Only for Production)
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)