from app.models import Variable
from django.shortcuts import redirect, render

from .Controller.CreateListVariableController import CreateListVariableController

from .forms import MyForm
from .models import Variable


# Create your views here.
def index(request):
    return render(request, 'index.html')


def createSimplex(request):
    if request.method == "GET":
        form = MyForm()    
        context = { 
            'form' : form
        }
        return render(request, 'createSimplex.html',context=context)

    else:
        form = MyForm(request.POST)
               

        CreateListVariableController(form.data['numeroRestricoes'], form.data['numeroVariaveisDecisao'])
        
        context = {}
        return redirect('problemVariables')


def problemVariables(request):
    return render(request, 'problemVariables.html')