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

def threePass(request):
    if request.session['IMethod'] == "GRAPHIC":
        return redirect('/grafica')
    else:
        return redirect('/tabular')
    
    
def tabular_view(request):
    try:
        json_request = make_json(request.session)
        json_request = json.dumps(json_request)
        json_response = simplex.main.solve_simplex(json_request)
        json_response = json.loads(json_response)

        if len(json_response["error_msg"]) > 0:
            raise Exception("Solution Error:" + json_response["error_msg"])

        headers = ["Base", "z"] + json_response["result"]["variables"] + ["b"]
        interactions = json_response["result"]["iterations"]
        optimum_point = json_response["result"]["optimum_point"]
        optimum_value = json_response["result"]["optimum_value"]
        tables = []

        for iter in interactions:
            current_table = []
            lineZ = ["z", "1"] + iter["z"]["coeficients"]
            lineZ.append(iter["z"]["value"])
            current_table.append(lineZ)

            for exp in iter["expressions"]:
                current_line = [exp["base"], "0"] + exp["coeficients"]
                current_line.append(exp["value"])
                current_table.append(current_line)

            tables.append(current_table)

        return render(request, 'resultado_tabular.html',
                      context={"tables": tables, "headers": headers, "optimum_point": optimum_point,
                               "optimum_value": optimum_value})
    except Exception as e:
        print(e)
        messages.error(request, 'Algo de inesperado aconteceu. Verifique as entradas.')
        return redirect('/')
