from django import forms
from .models import UserCustom,Genders,DocTypes

# Form Register Manager
class CustonRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserCustom

        # Form Input's
        fields = [
            'first_name',
            'last_name',
            'email',
            'num_doc',
            'num_tel',
            'id_tipo_documento',
            'id_genero',
            'fecha_nacimiento',
            'password'
        ]

        choices = Genders.objects.values_list('id', 'nombre')

        # Opciones para el campo id_tipo_documento
        choices = DocTypes.objects.values_list('id', 'nombre')