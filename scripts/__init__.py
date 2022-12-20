from Simplex import Simplex
from BranchAndBound import BranchAndBound
from SensitivityAnalysis import SensitivityAnalysis
import graphicalSolution as gs
import json

# Problema 1

z = [24, 22, 45]
restr = [[2, 1, 3], [2, 1, 2], [1, 0.5, 1]]
b = [[42], [40], [45]]
signal = ['<=', '<=', '<=']
t = Simplex(z, b, 3, 3, signal, restr, True, False)

# Problema 2
'''
z = [1, 2, 4]
restr= [[1, 4, 5],[1, 4, 1],[2, 0, 2]]
b = [[10], [8], [7]]
signal = ['<=','<=','<=']
t = Simplex(z, b, 3, 3, signal, restr, True, False)
'''

# Problema 3
'''
z = [7, 3]
restr= [[6, 4],[1, 2],[-1,1], [0,1],[-40, 10]]
b = [[24], [6], [2], [2], [5]]
signal = ['<=','<=','<=','<=','<=']
t = Simplex(z, b, 2, 5, signal, restr, True, False)
'''

# Problema 4
'''
z = [3, 2, 5]
restr = [[1, 2, 1], [3, 0, 2], [1, 4, 0]]
b = [[430], [460], [420]]
signal = ['<=', '<=', '<=']
t = Simplex(z, b, 3, 3, signal, restr, True, False)
'''
# Problema 5
'''
z = [2, 1, 3]
restr = [[5, 2, 7], [3, 2, 5]]
b = [[420], [280]]
signal = ['=', '>=']
t = Simplex(z, b, 3, 2, signal, restr, False, False)
'''
# Problema 6
'''
z = [3, 5]
restr= [[1, 0], [0, 2], [3, 2]]
b = [[4], [12], [18]]
signal = ['<=', '<=', '<=']
t = Simplex(z, b, 2, 3, signal, restr, True, False)
'''

# Problema 7
'''
z = [5, 8]    # z = 5x1 + 8x2
restr = [[1, 1], [5, 9]]  # x1 +x2 <= 6 | 5x1 + 9x2 <= 45
b = [[6], [45]]
signal = ['<=', '<=']
t = Simplex(z, b, 2, 2, signal, restr, True, False)
'''
'''
# Problema 8 - Radioterapico
z = [0.4, 0.5]  # z = 0.4x1 + 0.5x2
restr = [[0.3, 0.1],
         [0.5, 0.5],
         [0.6, 0.4]]
b = [[2.7], [6], [6]]
signal = ['<=', '=', '>=']
t = Simplex(z, b, 2, 3, signal, restr, False, False)
'''
'''
t.start()
q = BranchAndBound(False)
q.BAB(z, b, 2, 3, signal, restr, False)
q.result()
t.start()

if len(z) == 2:
    gs.plotagraf(z, gs.formatTable(restr, b), [0.5, 0.5], (-1, 10), (-1, 10))
'''

'''
z = [15, 12]
restr = [[1, 1], [8, 2]]
b = [[5], [17]]
signal = ['<=', '<=']
t = Simplex(z, b, 2, 2, signal, restr, True, False)
t.start()
solution = t.solution
'''
'''
q = BranchAndBound(True)
q.BAB(z, b, 2, 2, signal, restr, False)
q.result()
gs.plotagraf(z, gs.formatTable(restr, b), [0.5, 0.5], (-1, 10), (-1, 10), solution)
'''
t.start()
print(t.variable)
print(t.dict_result)
print(t.table)
print(t.Cb)
with open('../problem/result.json', 'w') as json_file:
    json.dump(t.dict_result, json_file, indent=4)
