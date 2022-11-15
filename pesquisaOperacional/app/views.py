from app.models import Variable
from django.shortcuts import redirect, render

from .Controller.CreateListVariableController import CreateListVariableController

from .forms import MyForm
from .models import Variable

nlin = 0
ncol = 0

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
        
        if form.is_valid():
            objectSimplex = form.cleaned_data 
            nlin = objectSimplex['numeroRestricoes']
            ncol = objectSimplex['numeroVariaveisDecisao']
            form.save()    
        context = {
            'form': form
        }
        return redirect('problemVariables')


def problemVariables(request):
    variable = Variable.objects.all()
    context = {
        "variable": variable
    }
    
    return render(request, 'problemVariables.html',context)

