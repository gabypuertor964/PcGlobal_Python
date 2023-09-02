from django.contrib import admin
from landing.models import DocTypes,Genders,Areas,States,Addresses

# Register your models here.
admin.site.register(DocTypes)
admin.site.register(Genders)
admin.site.register(Areas)
admin.site.register(States)
admin.site.register(Addresses)