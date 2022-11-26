from Simplex import Simplex

'''Até o momento presente o algoritmo está funcionando para os seguintes problemas:
Primal:
Problemas {1, 2, 3, 4, 5, 6}

Dual:
Problemas {5}

Os demais não foram testados devido ao site phpsimplex está fora do ar.
'''

# Problema 1
'''
z = [24, 22, 45]
restr= [[2, 1, 3],[2,1, 2], [1, 0.5, 1]]
b = [[42], [40], [45]]
signal = ['<=','<=','<=']
t = Simplex(z, b, 3, 3, signal, restr, True, False)
'''

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

z = [2, 1, 3]
restr = [[5, 2, 7], [3, 2, 5]]
b = [[420], [280]]
signal = ['=', '>=']
t = Simplex(z, b, 3, 2, signal, restr, False, False)

# Problema 6
'''
z = [3, 5]
restr= [[1, 0],[0, 2],[3, 2]]
b = [[4],[12],[18]]
signal = ['<=','<=','<=']
t = Simplex(z, b, 2, 3, signal, restr, True, False)
'''

# def __init__(self, z, b, num_var, num_restr, signal, restr, maximize, dual):
t.start()
t.result()
if t.error != '':
    print(t.error)
