from django import forms
#from .models import Variable
        
class MyForm(forms.Form):
    numeroRestricoes       =  forms.IntegerField(label='Número de Restrições',widget=forms.NumberInput(attrs={'class':'form-control'}))
    numeroVariaveisDecisao =  forms.IntegerField(label='Número de variáveis', widget=forms.NumberInput(attrs={'class':'form-control'}))
            
                            
class GenerateProblemSimplex(forms.Form):
    def __init__(self, numeroVariaveisDecisao, numeroRestricoes, *args, **kwargs):
        super(GenerateProblemSimplex, self).__init__(*args, **kwargs)

        
        for i in range(numeroVariaveisDecisao):
            if i != (numeroVariaveisDecisao - 1): # verify if i > 5
                self.fields[f'x{i}'] = forms.CharField(initial=0, label=f'x{i + 1} + ',
                                                       widget=forms.NumberInput(attrs={'class':'form-control'}))
                print(self.fields)
            else:
                self.fields[f'x{i}'] = forms.CharField(initial=0, label=f'x{i + 1}',
                                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))

        for i in range(numeroRestricoes):
            for j in range(numeroVariaveisDecisao + 2):
                if j == numeroVariaveisDecisao:
                    choices = [('<=', '<='), ('=', '='), ('>=', '>=')]
                    self.fields[f'a{i}{j}'] = forms.ChoiceField(choices=choices, label='signal', widget=forms.Select(attrs={'class':'form-control'}))
                elif j < numeroVariaveisDecisao:
                    if j != (numeroVariaveisDecisao - 1):
                        self.fields[f'a{i}{j}'] = forms.CharField(initial=0, label=f'x{j + 1} + ', widget=forms.NumberInput(attrs={'class':'form-control'}))
                    else:
                        self.fields[f'a{i}{j}'] = forms.CharField(initial=0, label=f'x{j + 1}',widget=forms.NumberInput(attrs={'class':'form-control'}))
                else:
                    self.fields[f'a{i}{j}'] = forms.CharField(initial=0, label=f'dontShow', widget=forms.NumberInput(attrs={'class':'form-control'}))