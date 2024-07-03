from django import forms
from . models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields=['nombre', 'email', 'mensaje']
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-Control'}),
            'email': forms.EmailInput(attrs={'class': 'form-Control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-Control'}),
        }

        