from django import forms
from .models import Variable
        
class MyForm(forms.Form):
    numeroRestricoes       =  forms.IntegerField(max_value=100)
    numeroVariaveisDecisao =  forms.IntegerField(max_value=100)
            
                            
class FormVariable: 
    class Meta: 
        model = Variable
        fields = ('numeroRestricoes','numeroVariaveisDecisao')
