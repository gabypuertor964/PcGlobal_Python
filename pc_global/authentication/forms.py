from django import forms
from .models import UserCustom, Genders, DocTypes

# Form Register Manager
class CustonRegistrationForm(forms.ModelForm):
    id_tipo_documento = forms.ModelChoiceField(queryset=DocTypes.objects.all(), label="Tipo de Documento")
    id_genero = forms.ModelChoiceField(queryset=Genders.objects.all(), label="Género")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

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
    
    # Validación de contraseña
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation', "Las contraseñas no coinciden")

        return cleaned_data