from Simplex import Simplex
from BranchAndBound import BranchAndBound
from SensitivityAnalysis import SensitivityAnalysis
import graphicalSolution as gs
import json
import time


def return_json(dict_result):
    with open('../problem/data.json', 'w') as json_file:
        json.dump(dict_result, json_file, indent=4)


def main(z, b, num_var, num_restr, signal, restr, maximize=True, dual=False, method='Tabular'):
    if method == 'Grafico':

        t = Simplex(z, b, num_var, num_restr, signal, restr, maximize, dual)
        t.start()
        if len(t.solution) == 3:
            gs.plotagraf(z, gs.formatTable(restr, b), [0.5, 0.5], (-1, 10), (-1, 10), t.solution)
        return_json(t.dict_result)

    if method == 'Tabular':
        t = Simplex(z, b, num_var, num_restr, signal, restr, maximize, dual)
        t.start()
        return_json(t.dict_result)

    if method == 'Integer':
        q = BranchAndBound(maximize)
        q.BAB(z, b, num_var, num_restr, signal, restr, dual)
        q.result()
        # (q.dict_result)


def read_json():
    try:
        # Opening JSON file
        file = open('../problem/dadosTest.json', )
        # returns JSON object as a dictionary
        data = json.load(file)
        data = data['data'][0]
        # Closing file
        file.close()
    except:
        time.sleep(3)
        read_json()

    objetivo = data['method']
    modo = data['option']
    tipo = data['type']
    z = []
    restr = []
    restr1 = []
    signal = []
    b = []

    for j in range(0, len(data['constraintsMethod'])):
        restr1 = []
        for i in range(0, len(data['numberVariablesMethod'])):
            restr1.append(float(data['numberVariablesMethod'][j][f'x{i + 1}']))
        restr.append(restr1)

        z.append(float(data['constraintsMethod'][f'x{j + 1}']))

        signal.append(data['numberVariablesMethod'][j][f'simbol'])

        b.append([float(data['numberVariablesMethod'][j][f'result'])])

    if modo == 'Maximizar':
        maximize = True
    else:
        maximize = False

    if modo == 'Dual':
        dual = True
    else:
        dual = False

    main(z, b, len(z), len(restr), signal, restr, maximize, dual, tipo)

read_json()