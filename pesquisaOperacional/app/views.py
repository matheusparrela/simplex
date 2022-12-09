#from app.models import Variable
from django.shortcuts import redirect, render
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
        for key in request.POST.keys():
            if key == 'csrfmiddlewaretoken':
                continue
            request.session[key] = request.POST[key]
        return redirect('problemVariables')

def problemVariables(request):
    
    if request.method == 'POST':
        numConstraints = int(request.session['numConstraints'])
        numVariable    =  int(request.session['numVariable'])
        
        request.session['objective'] = request.POST['objective']
        
        for i in range(numVariable):
            request.session[f'x{i}'] = request.POST[f'x{i}']

        for rows in range(numConstraints):
            for columns in range(numVariable + 2):
                request.session[f'x{rows}{columns}'] = request.POST[f'x{rows}{columns}']

        return redirect('/table')
    
    else:
        numVariable    = int(request.session['numVariable'])
        numConstraints = int(request.session['numConstraints'])
        context        = GenerateProblemSimplex(numVariable, numConstraints)

        return render(request, 'problemVariables.html', {
            'numVariable'  : range(numVariable),
            'numConstraints': range(numConstraints),
            'form'         : context,           
            'classCol'     : f'col-sm-{int(10 / (numVariable + 1))}',
            'sliceRest'    : f'{1 + numVariable}:',
            'sliceObjet'   : f'1:{numVariable + 1}'
        })

def table(request): 
    return redirect(request, 'table.html')
    