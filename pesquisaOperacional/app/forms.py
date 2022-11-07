from django import forms
from .models import Variable


        
class ServidorForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = ('numeroRestricoes', 'numerosVariaveisDecisao')
        widgets = {
            'numeroRestricoes': forms.TextInput(attrs={
                'class': 'form-control',
                'max_length': 2,
                'placeholder': 'number'
            }),
            'numerosVariaveisDecisao': forms.textInput(attrs={
                'class': 'form-control',
                'max_length': 2,
            })              
        }
        
