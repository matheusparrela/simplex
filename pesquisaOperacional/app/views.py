#from app.models import Variable
from django.shortcuts import redirect, render

from .Controller.CreateListVariableController import CreateListVariableController

from .forms import GenerateProblemSimplex, MyForm
#from .models import Variable


# Create your views here.
def index(request):
    return render(request, 'index.html')

def createSimplex(request):
    if request.method == "GET":
        request.session.flush()
        form = MyForm()    

        return render(request, 'createSimplex.html', {'form': form})

    else:
        #form = MyForm(request.POST)
        for key in request.POST.keys():
            if key == 'csrfmiddlewaretoken':
                continue
            request.session[key] = request.POST[key]
        return redirect('problemVariables')

def problemVariables(request):
    
    if request.method == 'POST':
        #recebo via request as duas veriaveis 
        numVariable   = int(request.session['numeroVariaveisDecisao'])
        numRestricoes = int(request.session['numeroRestricoes'])
    
        request.session['objective'] = request.POST['objective']
        for rows in range(numVariable):
            request.session[f'x{rows}'] = request.POST[f'x{rows}']

        for rows in range(numRestricoes):
            for columns in range(numVariable + 2):
                request.session[f'a{rows:02d}{columns:02d}'] = request.POST[f'a{rows:02d}{columns:02d}']

        return redirect('/table')
    
    else:
        numVariable   = int(request.session['numeroVariaveisDecisao'])
        numRestricoes = int(request.session['numeroRestricoes'])
        context = GenerateProblemSimplex(numVariable, numRestricoes)

        return render(request, 'problemVariables.html', {
            'form'         : context,
            'numVariable'  : range(numVariable),
            'numRestricoes': range(numRestricoes),
            'classCol'     : f'col-sm-{int(10 / (numVariable + 1))}',
            'sliceRest'    : f'{1 + numVariable}:',
            'sliceObjet'   : f'1:{numVariable + 1}'
        })

def table(request): 
    return redirect(request, 'table.html')
    