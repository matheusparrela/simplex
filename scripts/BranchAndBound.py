import math
from Simplex import Simplex
from Node import Node


class BranchAndBound:

    def __init__(self, maximize):
        self.root = Node(None, None, None)
        self.root = None
        self.table_solution = []
        self.maximize = maximize
        self.iteracao = -1
        self.int_solution = 0

    def integerSolution(self, solution):

        test = []
        for i in range(0, len(solution)):
            if math.trunc(solution[i]) == solution[i]:
                test.append(0)
            else:
                test.append(1)
        if len(set(test)) == 1 and test[1] != 1:
            return 'VIAVEL'
        else:
            return 'INVIAVEL'

    def viability(self, solution):

        if self.integerSolution(solution) == 'VIAVEL':
            return True
        else:
            return False

    def validityOfRestrictions(self, b, restr, signal, new_restr, new_signal, new_b):

        if new_restr in restr:
            if signal[restr.index(new_restr)] != new_signal:
                if b[restr.index(new_restr)][0] < new_b:
                    return True
        return False

    def result(self):
        print('\n|------------------Resultado B&B-----------------|\n')
        for i in range(0, len(self.table_solution)):
            print(self.table_solution[i])

        if self.maximize is True:
            self.int_solution = [-100000000000]
            for i in range(1, len(self.table_solution)):
                if self.table_solution[i][len(self.table_solution[0]) - 1] == 'VIAVEL':
                    if self.table_solution[i][0] <= self.table_solution[0][0]:
                        if self.table_solution[i][0] >= self.int_solution[0]:
                            self.int_solution = self.table_solution[i].copy()
        else:
            self.int_solution = [100000000000]
            for i in range(1, len(self.table_solution)):
                if self.table_solution[i][len(self.table_solution[0]) - 1] == 'VIAVEL':
                    if self.table_solution[i][0] >= self.table_solution[0][0]:
                        if self.table_solution[i][0] <= self.int_solution[0]:
                            self.int_solution = self.table_solution[i].copy()

        print('\nSolução Inteira:', self.int_solution)

    def BAB(self, z, b, num_var, num_restr, signal, restr, dual):

        novo = Node(Simplex(z, b, num_var, num_restr, signal, restr, self.maximize, dual), None, None)  # cria um Nó
        novo.item.start()
        self.table_solution.append(novo.item.solution.copy())
        self.iteracao += 1

        if novo.item.error == 'Erro 5 - Não existe solução.':
            self.table_solution[self.iteracao].append('IMPOSSIVEL')
            return 'IMPOSSIVEL'

        if self.root is None:  # Verifica se o primeiro nó da árvore existe
            self.root = novo

        atual = self.root  # se nao for a raiz

        '''Analisa a variavel a ser escolhida. Variante de Dank: O autor propõe que a variável a ser
        escolhida para a divisão seja a que possuir o maior resíduo.'''
        residue = []
        for i in range(1, len(novo.item.solution)):
            residue.append(novo.item.solution[i] - int(novo.item.solution[i]))

        if self.viability(novo.item.solution):
            self.table_solution[self.iteracao].append('VIAVEL')
            return novo.item.solution

        else:
            self.table_solution[self.iteracao].append('INVIAVEL')
            '''Monta a nova restrição para o problema'''
            new_restr = []
            for i in range(0, len(novo.item.solution) - 1):
                if i == residue.index(max(residue)):
                    new_restr.append(1)
                else:
                    new_restr.append(0)

            if novo.dir is None:
                new_signal = '>='
                new_b = int(novo.item.solution[residue.index(max(residue)) + 1]) + 1

                restr2 = restr.copy()
                signal2 = signal.copy()
                b2 = b.copy()

                # Analisa se as novas restrições são válidas ou impossíveis
                if not self.validityOfRestrictions(b, restr, signal, new_restr, new_signal, new_b):
                    restr2.append(new_restr)
                    signal2.append(new_signal)
                    b2.append([new_b])
                    self.BAB(z, b2, num_var, len(restr2), signal2, restr2, dual)
                else:
                    self.table_solution[self.iteracao].append('IMPOSSIVEL')
                    return 'IMPOSSIVEL'

            if novo.esq is None:  # Verificar a condição que determina qual o galhoa arvore deve seguir.

                new_signal = '<='
                new_b = int(novo.item.solution[residue.index(max(residue)) + 1])

                restr1 = restr.copy()
                signal1 = signal.copy()
                b1 = b.copy()

                # Analisa se as novas restrições são válidas ou impossíveis
                if not self.validityOfRestrictions(b, restr, signal, new_restr, new_signal, new_b):
                    restr1.append(new_restr)
                    signal1.append(new_signal)
                    b1.append([new_b])
                    self.BAB(z, b1, num_var,  len(restr1), signal1, restr1, dual)
                else:
                    self.table_solution[self.iteracao].append('IMPOSSIVEL')
                    return 'IMPOSSIVEL'
