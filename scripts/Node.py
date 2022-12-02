class Node:

    def __init__(self, key, esq, dir):
        self.item = key
        self.esq = esq
        self.dir = dir


import math
from Simplex import Simplex
from Node import Node


class BranchAndBound:

    def __init__(self, z, b, num_var, num_restr, signal, restr, maximize, dual):
        self.z = z  # Função a ser maximizada/minimizada
        self.b = b  # Lado direito das restrições
        self.num_var = num_var  # Número de variáveis
        self.num_restr = num_restr  # Número de restrições
        self.maximize = maximize  # Verifica se é uma maximização ou minimização
        self.dual = dual  # Verifica se a resolução é pelo dual ou primal
        self.restr = restr  # restrições
        self.signal = signal  # Sinais das restrições: <=, >=, =
        self.root = Node(None, None, None)
        self.root = None

    def integerSolution(self, solution):
        test = []
        for i in range(0, len(solution)):
            if math.trunc(solution[i]) == solution[i]:
                test.append(0)
            else:
                test.append(1)
        if len(set(test)) == 1 and test[1] != 1:
            return 'viavel'

        else:
            return 'inviavel'

    def viability(self, solution):

        if self.integerSolution(solution) == 'viavel':
            return True
        return False

    def validityOfRestrictions(self, new_restr, new_signal, new_b):

        if new_restr in self.restr:
            if self.signal[self.restr.index(new_restr)] != new_signal:
                if self.b[self.restr.index(new_restr)] < new_b:
                    return True

        return False

    def BAB(self):

        novo = Node(
            Simplex(self.z, self.b, self.num_var, self.num_restr, self.signal, self.restr, self.maximize, self.dual),
            None, None)
        novo.item.start()
        solution = novo.item.solution

        if self.viability(solution):
            return solution

        else:

            if self.root is None:
                self.root = novo

            '''Analisa a variavel a ser escolhida. Variante de Dank: O autor propõe que a variável a ser
            escolhida para a divisão seja a que possuir o maior resíduo.'''
            residue = []
            for i in range(1, len(novo.item.solution)):
                residue.append(novo.item.solution[i] - int(novo.item.solution[i]))

            '''Monta a nova restrição para o problema'''
            new_restr = []
            for i in range(0, len(solution) - 1):
                if i == residue.index(max(residue)):
                    new_restr.append(1)
                else:
                    new_restr.append(0)

            teste = []

            if novo.esq is None:  # Verificar a condição que determina qual o galhoa arvore deve seguir.
                new_signal = '>='
                new_b = int(solution[teste.index(max(teste))] + 1)

                '''Analisa se as novas restrições são válidas ou impossíveis'''
                if self.validityOfRestrictions(new_restr, new_signal, new_b):
                    self.restr.append(new_restr)
                    self.signal.append(new_signal)
                    self.b.append(new_b)

                    self.BAB()

            elif novo.dir is None:
                new_signal = '<='
                new_b = int(solution[teste.index(max(teste))] + 1) + 1

                '''Analisa se as novas restrições são válidas ou impossíveis'''
                if self.validityOfRestrictions(new_restr, new_signal, new_b):
                    self.restr.append(new_restr)
                    self.signal.append(new_signal)
                    self.b.append(new_b)
                    self.BAB()

            else:
                return 'impossivel'


