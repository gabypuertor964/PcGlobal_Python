from django.forms import ModelForm
from .models import Pqrs
from django import forms

class CreatePqrsForm(ModelForm):
    
    class Meta:
        model = Pqrs 
        
        fields = [
            'title', 'date_occurrence', 'id_tipo_pqrs',  'descripcion', 'evidence' 
        ]
        
        labels = {
            'title': 'Titulo del Reporte',
            'date_occurrence': 'Fecha del Problema',
            'id_tipo_pqrs':'Tipo del Reporte',
            'descripcion': 'Descripcion del Reporte',
            'evidence': 'Foto o Evidencia del Problema'
        }
        
        widgets = {
            'date_occurrence': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )
        
        self.fields['date_occurrence'].widget.attrs.update(
            {
                'class':'form-control',
                'placeholder': 'Por defecto la fecha de lo sucedido sera el dia de hoy'
            }
        )
        
        self.fields['id_tipo_pqrs'].widget.attrs.update(
            {
                'class':'form-control',
                'placeholder': 'Tipo de Reporte'
            }
        )
        
        self.fields['descripcion'].widget.attrs.update(
            {
                'class':'form-control',
                'placeholder':'Descripcion de lo sucedido'
            }
        )
        
        self.fields['evidence'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )
