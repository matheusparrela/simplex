from Simplex import Simplex
import numpy as np

#Problema 1
z = [24, 22, 45]
restr= [[2, 1, 3],[2,1, 2], [1, 0.5, 1]]
b = [42, 40, 45]
sinal = ['<=','<=','<=']


q = Simplex(z, b, 3, 3, sinal, restr, True)
print(np.round(q.solveSimplex(), decimals=3))


#Problema 2
'''
z = [1, 2, 4]
restr= [[1, 4, 5],[1, 4, 1],[2, 0, 2]]
b = [10, 8, 7]
sinal = ['<=','<=','<=']

r = Simplex(z, b, 3, 3, sinal, restr, True)
print(np.round(r.solveSimplex(), decimals=3))
'''

#Problema 3
'''
z = [7, 3]
restr= [[6, 4],[1, 2],[-1,1], [0,1],[-40, 10]]
b = [24, 6, 2, 2, 5]
sinal = ['<=','<=','<=','<=','<=']

s = Simplex(z, b, 2, 5, sinal, restr, False)
print(np.round(s.solveSimplex(), decimals=3))
'''


#Problema 4
'''
z = [3, 2, 5]
restr= [[1, 2, 1],[3, 0, 2],[1,4,0]]
b = [430, 460, 420]
sinal = ['<=','<=','<=',]

s = Simplex(z, b, 3, 3, sinal, restr, False)
print(np.round(s.solveSimplex(), decimals=3))
'''