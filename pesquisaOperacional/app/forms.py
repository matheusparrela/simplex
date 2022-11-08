from django import forms
from .models import Variable
        
class MyForm(forms.ModelForm):
    numeroRestricoes       =  forms.IntegerField()
    numeroVariaveisDecisao =  forms.IntegerField()
            
                
                
class FormVariable: 
    class Meta: 
        model = Variable
        fields = '__all__'
        

