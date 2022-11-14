from django.shortcuts import redirect, render
from app.models import Variable
from .models import Variable
from .forms import MyForm


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
        #form.data['numeroRestricoes']
        
        context = {}
        return render(request, 'index.html', context=context)


def problemVariables(request):
    return render(request, 'problemVariables.html')