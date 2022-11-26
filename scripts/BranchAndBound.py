from Simplex import Simplex
import numpy as np


def e(z, b, num_var, num_restr, signal, restr, maximize, dual):
    t = Simplex(z, b, num_var, num_restr, signal, restr, maximize, dual)
    t.start()
    solution = t.solution
    print('OI', solution)

    if not isinstance(solution, int):
        print('oi')
        teste = []

        for i in range(1, len(solution)):
            teste.append(solution[i] - int(solution[i]))

        nova_restr = []

        for i in range(0, len(solution)-1):
            if i == teste.index(max(teste)):
                nova_restr.append(1)
            else:
                nova_restr.append(0)

        restr.append(nova_restr)

        direita = b.copy()
        esquerda = b.copy()
        direita.append([int(solution[teste.index(max(teste))]+1)])
        esquerda.append([int(solution[teste.index(max(teste))]+1)+1])

        signal1 = signal.copy()
        signal2 = signal.copy()
        signal1.append('<=')
        signal2.append('>=')

        dir = Simplex(z, direita, num_var, len(direita), signal1, restr, maximize, dual)
        dir.start()
        esq = Simplex(z, esquerda, num_var, len(esquerda), signal2, restr, maximize, dual)
        esq.start()

    else:
        print('tchau')
