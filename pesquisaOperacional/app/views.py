from django.shortcuts import redirect, render
from app.models import Variable
from django.views.generic import ListView
from .models import Variable
from .forms import ServidorForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def createSimplex(request):
    if request.method == 'GET':
        variables = Variable.objects.all()
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'createSimplex.html', context=context)
    
    else:
        form2 = ServidorForm(request.POST, request.FILES)
        form2.save()
        return redirect('') 
    
    
    
    
    
    
    return render(request, "createSimplex.html",{"variable": variables}) 

