from django.contrib import admin
from landing.models import docTypes,genders,areas,states,addresses

# Register your models here.
admin.site.register(docTypes)
admin.site.register(genders)
admin.site.register(areas)
admin.site.register(states)
admin.site.register(addresses)