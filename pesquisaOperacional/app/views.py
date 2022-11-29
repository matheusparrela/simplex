#from app.models import Variable
from django.shortcuts import redirect, render

from .Controller.CreateListVariableController import CreateListVariableController

from .forms import GenerateProblemSimplex, MyForm
#from .models import Variable

nlin = 0
ncol = 0

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
        numVariable = int(request.session['numeroVariaveisDecisao'])
        numRestricoes = int(request.session['numeroRestricoes'])
        url = '/table'

        request.session['objective'] = request.POST['objective']

        for i in range(numVariable):
            request.session[f'x{i}'] = request.POST[f'x{i}']

        for i in range(numRestricoes):
            for j in range(numVariable + 2):
                request.session[f'a{i}{j}'] = request.POST[f'a{i}{j}']

        return redirect(url)
    else:
        numVariable = int(request.session['numeroVariaveisDecisao'])
        numRestricoes = int(request.session['numeroRestricoes'])
        form = GenerateProblemSimplex(numVariable, numRestricoes)

        return render(request, 'problemVariables.html', {'form': form, 'numVar': range(numVariable), 'numRest': range(numRestricoes)
                      , 'classCol': f'col-sm-{int(10 / (numVariable + 1))}', 'sliceRest': f'{1 + numVariable}:'
                      , 'sliceObjet': f'1:{numVariable + 1}'})

def table(request): 
    return redirect(request, 'table.html')
    