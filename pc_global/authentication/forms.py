from .models import UserCustom
from django import forms

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
            'fecha_nacimiento'
        ]