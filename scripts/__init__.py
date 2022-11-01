from Simplex import Simplex
import numpy as np
'''Até o momento presente o algoritmo está funcionando para os seguintes problemas:
Problemas {1, 2, 3, 4, 5, 6}

Os demais não foram testados devido ao site phpsimplex está fora do ar.
'''

#Problema 1
'''
z = [24, 22, 45]
restr= [[2, 1, 3],[2,1, 2], [1, 0.5, 1]]
b = [[42], [40], [45]]
sinal = ['<=','<=','<=']
t = Simplex(z, b, 3, 3, sinal, restr, True, False)
'''

#Problema 2
'''
z = [1, 2, 4]
restr= [[1, 4, 5],[1, 4, 1],[2, 0, 2]]
b = [[10], [8], [7]]
sinal = ['<=','<=','<=']
t = Simplex(z, b, 3, 3, sinal, restr, True, False)
'''

#Problema 3
'''
z = [7, 3]
restr= [[6, 4],[1, 2],[-1,1], [0,1],[-40, 10]]
b = [[24], [6], [2], [2], [5]]
sinal = ['<=','<=','<=','<=','<=']
t = Simplex(z, b, 2, 5, sinal, restr, True, False)
'''

#Problema 4
'''
z = [3, 2, 5]
restr= [[1, 2, 1],[3, 0, 2],[1,4,0]]
b = [[430], [460], [420]]
sinal = ['<=','<=','<=',]
t = Simplex(z, b, 3, 3, sinal, restr, True, False)
'''

#Problema 5

z = [2, 1, 3]
restr= [[5, 2, 7],[3,2, 5]]
b = [[420], [280]]
sinal = ['=','>=']
t = Simplex(z, b, 3, 2, sinal, restr, True, False)


#Problema 6
'''
z = [3, 5]
restr= [[1, 0],[0, 2],[3, 2]]
b = [[4],[12],[18]]
sinal = ['<=','<=','<=']
t = Simplex(z, b, 2, 3, sinal, restr, True, False)
'''

t.start()
print('Base:', t.base)
print('Função Objetivo:', t.z)
print('Função Artificial:', t.arti_function)
print('Cb:', t.Cb)
print(t.variable)
t.result()