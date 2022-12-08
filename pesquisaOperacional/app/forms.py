from django import forms
#from .models import Variable
        
class MyForm(forms.Form):
    # interface para escolher metodo
    IMethod = [
        ('PRIMAL', 'Primal'),
        ('DUAL', 'Dual')
    ]
    selectSolution         = forms.BooleanField(label="Utilizar solução inteira", required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    numeroRestricoes       = forms.IntegerField(label='Número de Restrições',widget=forms.NumberInput(attrs={'class':'form-control'}))
    numeroVariaveisDecisao = forms.IntegerField(label='Número de variáveis', widget=forms.NumberInput(attrs={'class':'form-control'}))
    method                 = forms.ChoiceField(choices=IMethod, widget=forms.RadioSelect(attrs={'class':'form-check-input'}), label='Método')
    
                            
class GenerateProblemSimplex(forms.Form):
    def __init__(self, numeroVariaveisDecisao, numeroRestricoes, *args, **kwargs):
        super(GenerateProblemSimplex, self).__init__(*args, **kwargs)
        
        objectiveFunction = [('MAXIMIZE', 'Maximizar'), ('MINIMIZE', 'Minimizar')]
        self.fields['objective'] = forms.ChoiceField(choices= objectiveFunction, label='objective', widget=forms.Select(attrs={'class':'form-control'}))
               

        for rows in range(numeroVariaveisDecisao ):
            if rows != (numeroVariaveisDecisao-1): # check if i > 5
                self.fields[f'x{rows:02d}'] = forms.DecimalField(label=f'x{rows + 1} + ',initial=0,
                    widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':f'x{rows + 1}'}))
                
            else:
                self.fields[f'x{rows}'] = forms.DecimalField( label=f'x{rows+1}', initial=0,
                    widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':f'x{rows + 1}'}))

        for rows in range(numeroRestricoes):
            for columns in range(numeroVariaveisDecisao + 2):
                if columns == numeroVariaveisDecisao:
                    choices = [('<=', '<='), ('=', '='), ('>=', '>=')]
                    self.fields[f'{rows}{columns}'] = forms.ChoiceField(choices=choices, label='signal', widget=forms.Select(attrs={'class':'form-control'}))
                elif columns < numeroVariaveisDecisao:
                    if columns != (numeroVariaveisDecisao - 1):
                        self.fields[f'a{rows}{columns}'] = forms.DecimalField(label=f'x{columns + 1} + ', widget=forms.NumberInput(attrs={'class':'form-control'}))
                    else:
                        self.fields[f'a{rows}{columns}'] = forms.DecimalField(label=f'x{columns + 1}',widget=forms.NumberInput(attrs={'class':'form-control'}))
                else:
                    self.fields[f'a{rows}{columns}'] = forms.DecimalField(label=f'break', widget=forms.NumberInput(attrs={'class':'form-control'}))  