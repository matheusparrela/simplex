from Simplex import Simplex


#Problema 
z = [24, 22, 45]
restr= [[2, 1, 3],[2,1, 2], [1, 0.5, 1]]
b = [42, 40, 45]
sinal = ['<=','<=','<=']


q = Simplex(z, b, 3, 3, sinal, restr, True)
print(q.solveSimplex())