from .models import UserCustom
from django import forms

# Form Register Manager
class CustonRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserCustom

        # Form Input's
        fields = '__all__'