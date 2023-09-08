from import_export import resources 
from authentication.models import DocTypes

class DocTypesResource(resources.ModelResource):
    class Meta:
        model = DocTypes
        fields = ('nombre', 'siglas')
