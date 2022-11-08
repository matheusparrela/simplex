from django import forms
from .models import Variable
        
class MyForm(forms.ModelForm):
    'numeroRestricoes': forms.IntegerField(max_lenght=3)
    'numeroVariaveisDecisao': forms.IntegerField(max_lenght=3)
                
                
                
class FormVariable: 
    class Meta: 
        model = Variable
        fields = '__all__'
        

