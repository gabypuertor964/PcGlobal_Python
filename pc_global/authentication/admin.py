from django.contrib import admin

# Register your models here.
from authentication.models import DocTypes,Genders,Addresses,UserCustom

# Register your models here.
admin.site.register(DocTypes)
admin.site.register(Genders)
admin.site.register(Addresses)
admin.site.register(UserCustom)