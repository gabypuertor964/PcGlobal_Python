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

    # Pqrs URLS
    path('pqrs/', include('pqrs.urls'))
]

# Static and Media URLs (Only for Production)
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Error Handlers / Custom Error Pages
handler404 = 'landing.views.handler404'
handler500 = 'landing.views.handler500'
handler403 = 'landing.views.handler403'
handler400 = 'landing.views.handler400'
handler401 = 'landing.views.handler401'
handler408 = 'landing.views.handler408'
