import math
from Simplex import Simplex
from Node import Node


class BranchAndBound:

    def __init__(self, z, b, num_var, num_restr, signal, restr, maximize, dual):
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
            return 'VIAVEL'

        else:
            return 'INVIAVEL'

    def viability(self, solution):

        if self.integerSolution(solution) == 'VIAVEL':
            return True

        return False

    def validityOfRestrictions(self, b, restr, signal, new_restr, new_signal, new_b):

        if new_restr in restr:
            if signal[restr.index(new_restr)] != new_signal:
                if b[restr.index(new_restr)][0] < new_b:
                    return True
        return False


    def result(self):
        pass


    def BAB(self, z, b, num_var, num_restr, signal, restr, maximize, dual):

        novo = Node(Simplex(z, b, num_var, num_restr, signal, restr, maximize, dual), None, None)  # cria um Nó
        novo.item.start()
        if novo.item.error != '':
            print(novo.item.error)
        
        if novo.item.error == 'Erro 5 - Não existe solução.':
            return 'IMPOSSIVEL'


        if self.viability(novo.item.solution):
            return novo.item.solution

        atual = self.root  # se nao for a raiz

        '''Analisa a variavel a ser escolhida. Variante de Dank: O autor propõe que a variável a ser
        escolhida para a divisão seja a que possuir o maior resíduo.'''
        residue = []
        for i in range(1, len(novo.item.solution)):
            residue.append(novo.item.solution[i] - int(novo.item.solution[i]))

        '''Monta a nova restrição para o problema'''
        new_restr = []
        for i in range(0, len(novo.item.solution) - 1):
            if i == residue.index(max(residue)):
                new_restr.append(1)
            else:
                new_restr.append(0)

        if self.root is None:  # Verifica se o primeiro nó da árvore existe
            self.root = novo
            #  self.BAB(z, b1, num_var, num_restr + 1, signal1, restr1, maximize, dual)

        if novo.dir is None:
            new_signal = '>='
            new_b = int(novo.item.solution[residue.index(max(residue))+ 1]) + 1

            restr2 = restr.copy()
            signal2 = signal.copy()
            b2 = b.copy()

            # Analisa se as novas restrições são válidas ou impossíveis
            if not self.validityOfRestrictions(b, restr, signal, new_restr, new_signal, new_b):
                restr2.append(new_restr)
                signal2.append(new_signal)
                b2.append([new_b])
                z.pop()
                z.pop()
                z.pop()
                self.BAB(z, b2, num_var, len(restr2), signal2, restr2, maximize, dual)

            else:
                return 'IMPOSSIVEL'

        if novo.esq is None:  # Verificar a condição que determina qual o galhoa arvore deve seguir.

            new_signal = '<='
            new_b = int(novo.item.solution[residue.index(max(residue))+ 1])

            restr1 = restr.copy()
            signal1 = signal.copy()
            b1 = b.copy()

            # Analisa se as novas restrições são válidas ou impossíveis
            if not self.validityOfRestrictions(b, restr, signal, new_restr, new_signal, new_b):
                restr1.append(new_restr)
                signal1.append(new_signal)
                b1.append([new_b])
                z.pop()
                z.pop()
                z.pop()
                self.BAB(z, b1, num_var,  len(restr2), signal1, restr1, maximize, dual)

            else:
                return 'IMPOSSIVEL'
