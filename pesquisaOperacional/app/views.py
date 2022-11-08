from django.shortcuts import redirect, render
from app.models import Variable
from .models import Variable
from .forms import FormVariable


# Create your views here.
def index(request):
    return render(request, 'index.html')


def createSimplex(request):
    form = FormVariable()
    context = {
        'form': form
    }
    
    return render(request, 'createSimplex.html',context = context)

