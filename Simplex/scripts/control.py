from Simplex import Simplex
from BranchAndBound import BranchAndBound
from SensitivityAnalysis import SensitivityAnalysis
import graphicalSolution as gs
import json


def read_json():
    # Opening JSON file
    file = open('../problem/problem.json', )
    # returns JSON object as a dictionary
    data = json.load(file)
    # Closing file
    file.close()


def return_json(dict_result):
    with open('Simplex/problem/data.json', 'w') as json_file:
        json.dump(dict_result, json_file, indent=4)


def main(z, b, num_var, num_restr, signal, restr, maximize=True, dual=False, method='Tabular'):

    if method == 'grafico':

        t = Simplex(z, b, num_var, num_restr, signal, restr, True, False)
        t.start()
        if len(t.solution) == 3:
            gs.plotagraf(z, gs.formatTable(restr, b), [0.5, 0.5], (-1, 10), (-1, 10), t.solution)

    if method == 'Tabular':
        t = Simplex(z, b, num_var, num_restr, signal, restr, True, False)
        t.start()
        return_json(t.dict_result)

    if method == 'Integer':
        q = BranchAndBound(True)
        q.BAB(z, b, num_var, num_restr, signal, restr, False)
        q.result()
        # (q.dict_result)
