from django import forms
#from .models import Variable
        
class MyForm(forms.Form):
    # interface para escolher metodo
    IMethodModule = [
        ('GRAPHIC', 'Gráfica'),
        ('TABULAR', 'Tabular')
    ]
    
    IMethod = [
        ('PRIMAL', 'Primal'),
        ('DUAL', 'Dual')
    ]
    selectModule   = forms.ChoiceField(choices = IMethodModule, initial= IMethodModule[1], widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'onchange': 'VerificaVal()','id': 'tipo'}), label='Tipo')
    selectSolution = forms.BooleanField(label="Utilizar solução inteira", required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    numConstraints = forms.IntegerField(label='Número de Restrições',widget=forms.NumberInput(attrs={'class':'form-control'}))
    numVariable    = forms.IntegerField(label='Número de variáveis', widget=forms.NumberInput(attrs={'class':'form-control'}))
    method         = forms.ChoiceField(choices=IMethod, widget=forms.RadioSelect(attrs={'class':'form-check-input'}), label='Método')
    
                            
class GenerateProblemSimplex(forms.Form):
    def __init__(self, numVariable, numConstraints, *args, **kwargs):
        super(GenerateProblemSimplex, self).__init__(*args, **kwargs)
        
        objectiveFunction = [('MAXIMIZE', 'Maximizar'), ('MINIMIZE', 'Minimizar')]
        self.fields['objective'] = forms.ChoiceField(choices= objectiveFunction, label='objective', widget=forms.Select(attrs={'class':'form-control'}))
               

        for rows in range(numVariable ):
            if rows != (numVariable-1): # check if i > 5
                self.fields[f'x{rows:02d}'] = forms.DecimalField(label=f'x{rows + 1} + ',initial=0,
                    widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':f'x{rows + 1}'}))
                
            else:
                self.fields[f'x{rows}'] = forms.DecimalField( label=f'x{rows+1}', initial=0,
                    widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':f'x{rows + 1}'}))

        for rows in range(numConstraints):
            for columns in range(numVariable + 2):
                if columns == numVariable:
                    choices = [('<=', '<='), ('=', '='), ('>=', '>=')]
                    self.fields[f'{rows}{columns}'] = forms.ChoiceField(choices=choices, label='signal', widget=forms.Select(attrs={'class':'form-control'}))
                elif columns < numVariable:
                    if columns != (numVariable - 1):
                        self.fields[f'n{rows}{columns}'] = forms.DecimalField(
                            label=f'x{columns + 1} +', widget=forms.NumberInput(attrs={'pattern':'[0-9]+$','class':'form-control','placeholder':f'x{columns + 1}',}))
                    else:
                        self.fields[f'n{rows}{columns}'] = forms.DecimalField(
                            label=f'x{columns + 1}',widget=forms.NumberInput(attrs={'pattern':'[0-9]+$', 'class':'form-control','placeholder':f'x{columns + 1}',}))
                else:
                    self.fields[f'n{rows}{columns}'] = forms.DecimalField(label=f'break', widget=forms.NumberInput(attrs={'class':'form-control'}))  