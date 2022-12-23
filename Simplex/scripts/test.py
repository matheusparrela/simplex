import numpy as np
import json

class Simplex:

    def __init__(self, z, b, num_var, num_restr, signal, restr, maximize, dual):
        self.z = z.copy()  # Função a ser maximizada/minimizada
        self.b = b.copy()  # Lado direito das restrições
        self.num_var = num_var  # Número de variáveis
        self.num_restr = num_restr  # Número de restrições
        self.maximize = maximize  # Verifica se é uma maximização ou minimização
        self.dual = dual  # Verifica se a resolução é pelo dual ou primal
        self.restr = restr.copy()  # restrições
        self.signal = signal.copy()  # Sinais das restrições: <=, >=, =
        self.table = []  # Tabela para execução do método simplex
        self.base = []  # Indice de X para os valores básicos
        self.Cb = []  # Valores em Z das variáveis básicas
        self.artificial = False  # Avalia se exixte alguma variavel artificial para usar o método das duas fases
        self.base_init = []  # Base inicial do problema para ser aplicado na segunda fase do problema
        self.arti_function = []  # Função das Variáveis artificiais
        self.novo_z = []  # Novo Z calculado para operração do método das duas fases
        self.variable = []  # Lista com as variaveis utilizadas durante a execução do problema
        self.exit = False  # Controle a saida do loop de execução
        self.error = ''  # Informa qual erro ocorreu na execução do problema
        self.var_artificial = []  # Recebe as variaveis artificiais do problema
        self.solution = []  # Armazena a solução do problema
        self.pos_pivo = []  # Contém a posição do pivô
        self.artificial_position = []
        self.dict_result = []
        self.iteracao = 0
        self.fuction_fase = None

    '''Método construtor da Classe'''
    '''Análisa se a solução já foi encontrada'''

    def out(self):

        if np.round(self.table[len(self.table) - 1:, 0:-1].min(), decimals=5) >= 0 or self.exit == True:
            return True
        else:
            return False

    '''Método que adiciona variaveis de folga, excesso e artificial'''

    def addVariables(self):

        self.table = np.matrix(self.restr, float)
        j = 1
        for i in range(0, len(self.restr)):

            # Adiciona variáveis: +artificial e -excesso
            if self.signal[i] == '>=':
                matriz = np.zeros((self.num_restr, 2))
                matriz[i, 0] = -1
                matriz[i][1] = 1
                self.artificial = True
                self.arti_function.append(0)
                self.arti_function.append(-1)
                self.Cb.append(-1)
                self.variable.append(f'X{i + self.num_var + j}')
                j += 1
                self.variable.append(f'X{i + self.num_var + j}')
                self.var_artificial.append(f'X{i + self.num_var + j}')
                self.artificial_position.append(i + self.num_var + j)

            # Adiciona variáveis: +artificial
            elif self.signal[i] == '=':
                matriz = np.zeros((self.num_restr, 1))
                matriz[i, 0] = 1
                self.artificial = True
                self.arti_function.append(-1)
                self.Cb.append(-1)
                self.variable.append(f'X{i + self.num_var + j}')
                self.var_artificial.append(f'X{i + self.num_var + j}')
                self.artificial_position.append(i + self.num_var + j)

            # Adiciona variáveis: +folga
            elif self.signal[i] == '<=':
                matriz = np.zeros((self.num_restr, 1))
                matriz[i, 0] = 1
                self.Cb.append(0)
                self.variable.append(f'X{i + self.num_var + j}')
                self.arti_function.append(0)

            self.table = np.concatenate(([self.table, matriz]), axis=1)
            self.base.append(f'X{self.table.shape[1]}')
            self.base_init.append(self.table.shape[1])

    '''Oraganiza a função a ser otimizada'''

    def objectiveFunction(self):

        for i in range(0, self.table.shape[1] - len(self.z)):
            self.z.append(0)

        '''Organiza a função objetivo caso exista variáveis artificiais'''
        if self.artificial:

            for i in range(0, self.num_var):
                self.arti_function = [0] + self.arti_function

            self.arti_function.append(0)

            for i in range(0, self.table.shape[1]):
                soma = 0
                for j in range(0, len(self.table)):
                    soma = soma + self.Cb[j] * self.table[j, i]

                soma = soma - self.arti_function[i]
                self.novo_z.append(soma)
        else:
            self.novo_z = np.array(self.z) * -1

    '''Fase II - Atualiza a função objetivo'''

    def objectiveFunctionFaseII(self):

        for i in range(0, self.table.shape[1]):
            soma = 0
            for j in range(0, len(self.Cb)):
                soma = soma + self.Cb[j] * self.table[j, i]
            soma = soma - self.z[i]
            self.table[len(self.table) - 1, i] = soma

    '''Organiza a tabela para aplicação do método simplex'''

    def organizeTable(self):

        self.negative()

        '''Variaveis do problema'''
        for i in range(0, self.num_var):
            self.variable.append(f'X{i + 1}')

        '''Organiza a tabela para ser aplicado o método dual'''
        if self.dual:
            self.dualSimplex()

        self.addVariables()
        self.table = np.hstack([self.table, self.b])

        '''Modifica a função objetivo para realizar a minimização do problema'''
        if not self.maximize:
            for i in range(0, len(self.z)):
                self.z[i] = self.z[i] * -1

        self.objectiveFunction()
        self.fuction_fase = self.arti_function.copy()
        self.table = np.vstack([self.table, self.novo_z])

        '''Para o passo II - elimina coluna das variáveis artificiais (Caso resrição >= ou =)'''
        self.base_init = sorted(self.base_init)

    '''A base ainda não está muito bem definida, atualizarei depois'''

    def basicVariablesFaseII(self):

        self.base[self.pos_pivo[0]] = self.variable[self.pos_pivo[1]]
        self.Cb[self.pos_pivo[0]] = self.z[self.pos_pivo[1]]

    def basicVariablesFaseI(self):

        self.base[self.pos_pivo[0]] = self.variable[self.pos_pivo[1]]
        self.Cb[self.pos_pivo[0]] = self.arti_function[self.pos_pivo[1]]

    '''Método de resolução usando o simplex'''

    def start(self):

        self.organizeTable()

        '''Se existir variáveis artificiais resolvemos usando o método das duas fases'''
        if self.artificial:
            '''Enquanto Z diferente de 0'''

            while (np.round(self.table[self.table.shape[0] - 1, self.table.shape[1] - 1], decimals=3) != 0) and (
                    not self.out()):
                self.solveSimplex()
                self.basicVariablesFaseI()

            self.pos_pivo = []
            self.retorno()

            if np.round(self.table[self.table.shape[0] - 1, self.table.shape[1] - 1], decimals=3) == 0:
                '''Apaga as colunas das variáveis artificiais para aplicar a 2 fase'''

                self.fuction_fase = self.z.copy()
                self.fuction_fase.pop()

                for i in range(0, len(self.artificial_position)):
                    self.table = np.delete(self.table, self.artificial_position[i] - i - 1, axis=1)
                    self.variable.pop(self.artificial_position[i] - i - 1)
                    self.fuction_fase.pop()
                self.exit = False

            '''Fase II'''

            if self.maximize is False:
                for i in range(0, len(self.Cb)):
                    self.Cb[i] = self.z[int(self.base[i][1]) - 1]

            self.objectiveFunctionFaseII()

        '''Enquanto existir na função objetivo Z valores menores que 0'''

        while not self.exit:
            self.solveSimplex()
            self.exit = self.out()
            '''Atualiza as variaveis da base'''
            self.basicVariablesFaseII()
            self.iteracao += 1

        self.pos_pivo = []
        self.retorno()
        self.noSolution()
        self.infiniteSolutions()
        self.result()


    '''Método de resolução usando o simplex'''

    def solveSimplex(self):

        self.pos_pivo = []
        list = []

        for i in range(0, len(self.table) - 1):
            '''Leva em consideração que esta operação só será realizada quando Pj superior a 0.'''
            '''Procura a coluna com o número mais negativo. Após isso, procura o menor valor positivo para a divisão 
            entre o b (termo independente) e a coluna selecionada anteriormente '''
            if self.table[
                i, np.where(self.table[len(self.table) - 1:, 0:-1] == self.table[len(self.table) - 1:, 0:-1].min())[1][
                    0]] > 0:
                try:
                    list.append(self.table[i, self.table.shape[1] - 1] / self.table[i, np.where(
                        self.table[len(self.table) - 1:, 0:-1] == self.table[len(self.table) - 1:, 0:-1].min())[1][0]])

                except ArithmeticError:
                    self.error = "Erro 1 - Problema na escolha do Pivô."
            else:
                list.append(100000000000)

        self.pos_pivo.append((list.index(min(list))))
        self.pos_pivo.append(
            np.where(self.table[len(self.table) - 1:, 0:-1] == self.table[len(self.table) - 1:, 0:-1].min())[1][0])

        self.retorno()

        '''Solução ilimitada (unbounded): se toda coluna da variável que entra na base tem todos os seus elementos 
        negativos ou nulos, trata-se de um problema não-limitado, ou seja, que tem solução ilimitada. Não há valor 
        ótimo concreto para a função objetivo, mas à medida que os valores das variáveis são aumentados, 
        o valor Z também aumenta sem violar qualquer restrição. '''
        if np.round(self.table[0:-1, self.pos_pivo[1]].max(), decimals=5) <= 0:
            self.error = 'Erro 2 - Solução ilimitada -(unbounded).'
            self.exit = True

        pivo = self.table[self.pos_pivo[0], self.pos_pivo[1]]

        if pivo != 0:
            '''Realiza o manipulação das linhas'''
            for i in range(0, len(self.table)):

                mult = -float(self.table[i, self.pos_pivo[1]]) / float(pivo)

                for j in range(0, self.table.shape[1]):
                    if i == self.pos_pivo[0]:
                        continue
                    if i == len(self.table) - 1:
                        self.table[i, j] = mult * self.table[self.pos_pivo[0], j] + self.table[i, j]
                        self.table[self.pos_pivo[0], j] = self.table[self.pos_pivo[0], j] / pivo
                    else:
                        self.table[i, j] = mult * self.table[self.pos_pivo[0], j] + self.table[i, j]
        else:
            '''Pivo é igual a zero'''
            self.error = 'Erro 3 - Pivô nulo ou negativo.'

    def result(self):

        # Se o problema é de minimização, o resultado tem que ser multiplicado por -1
        if not self.maximize:
            self.table[self.table.shape[0] - 1, self.table.shape[1] - 1] = self.table[self.table.shape[0] - 1,
                                                                                      self.table.shape[1] - 1] * -1

        print('\n|--------------------Resultado-------------------|')
        print('Z =', np.round(self.table[self.table.shape[0] - 1, self.table.shape[1] - 1], decimals=3))
        self.solution.append(np.round(self.table[self.table.shape[0] - 1, self.table.shape[1] - 1], decimals=3))
        for i in range(0, self.num_var):

            if self.variable[i] in self.base:
                self.solution.append(
                    np.round(self.table[self.base.index(self.variable[i]), self.table.shape[1] - 1], decimals=3))
                print(
                    f'{self.variable[i]} = {np.round(self.table[self.base.index(self.variable[i]), self.table.shape[1] - 1], decimals=3)}')
            else:
                self.solution.append(0)
                print(f'{self.variable[i]} = 0')

        self.result_json()

        if self.error != '':
            print(self.error)

    '''Modifica a tabela simplex para utilizar o método na sua forma dual'''

    def dualSimplex(self):

        for i in range(0, len(self.restr)):
            if self.signal[i] == '=':
                self.restr.append(self.restr[i].copy())
                for j in range(0, self.num_var):
                    self.restr[i][j] = self.restr[i][j] * -1
                self.signal[i] = '<='
                self.signal.append('<=')
                self.b.append([self.b[i][0]])
                self.b[i][0] = self.b[i][0] * -1

            if self.signal[i] == '<=':
                self.signal[i] = '>='
                for j in range(0, self.num_var):
                    self.restr[i][j] = self.restr[i][j] * -1
                self.b[i][0] = self.b[i][0] * -1

        c = np.transpose(self.restr)
        self.restr = c.tolist()

        temp = self.z

        self.z = []
        for i in range(0, len(self.b)):
            self.z.append(self.b[i][0])

        self.b = []
        self.signal = []
        self.num_var = len(self.z)
        self.num_restr = len(self.restr)

        if self.maximize:
            self.maximize = False
        else:
            self.maximize = True

        '''Consideramos aqui que as variaveis dos problemas resolvidos serão sempre do tipo X >= 0'''
        for i in range(0, self.num_restr):
            self.b.append([temp[i]])
            self.signal.append('<=')

    '''Para que um modelo esteja na forma padrão, o valor à direita de uma equação ou inequação deve ser sempre 
    não-negativo. Então, caso haja equações do tipo: A primeira coisa que devemos fazer é multiplicar os dois lados 
    da equação e inequação por (-1): '''

    def negative(self):

        for i in range(0, self.num_restr):
            if self.b[i][0] < 0:
                self.restr = np.array(self.restr)
                self.restr[i, 0:] *= -1
                self.restr = self.restr.tolist()
                self.b[i][0] *= -1

                if self.signal[i] == '<=':
                    self.signal[i] = '>='
                elif self.signal[i] == '>=':
                    self.signal[i] = '<='

    '''Soluções infinitas: satisfeito o critério de parada, se alguma variável de decisão não-básica tem um valor 0 
    na fila Z, significa que existe outra solução que fornece o mesmo valor ótimo para a função objetivo. Neste caso, 
    o problema admite infinitas soluções, todas as quais abrangidas dentro do segmento (ou parte do plano, 
    região de espaço, etc., conforme o número de variáveis do problema) definido por A·X1 + B·X2 = Z0. Através de uma 
    nova iteração e fazendo com que a variável de decisão que tenha 0 na linha Z entre na base, é obtida uma solução 
    diferente para o mesmo valor ótimo. '''

    def infiniteSolutions(self):

        for i in range(0, self.num_var):
            if self.variable[i] not in self.base:
                if np.round(self.table[self.table.shape[0] - 1, self.variable.index(self.variable[i])],
                            decimals=5) == 0:
                    self.error = 'Erro 4 - Infinitas Soluções.'

    '''Não existe solução: quando nenhum ponto satisfaz às restrições do problema, ocorre a inviabilidade, 
    não existindo nenhuma solução possível para ele. Neste caso, uma vez terminadas todas as iterações do algoritmo, 
    existem na base variáveis artificiais em que o valor é superior a zero. (os valores são indicados na coluna Xn)'''

    def noSolution(self):

        for i in range(0, len(self.base)):
            if self.base[i] in self.var_artificial:
                if self.table[self.base.index(self.base[i]), self.table.shape[1] - 1] > 0:
                    self.error = 'Erro 5 - Não existe solução.'

    def retorno(self):

        var = self.variable.copy()
        var.append('b')
        var = ['Cb'] + var

        Cb = np.round(self.Cb.copy(), decimals=3).tolist()
        table = np.round(self.table.copy(), decimals=3).tolist()

        for i in range(0, len(Cb)):
            table[i].insert(0, Cb[i])

        iter = {'base': self.base,
                'variable': var,
                'table': table,
                'erro': self.error,
                'z': self.fuction_fase,
                'pivo': self.pos_pivo
                }
        self.dict_result.append(iter)


    def result_json(self):

        dict = {}
        self.variable.insert(0, 'Z')
        for i in range(0, len(self.solution)):
            dict[f'{self.variable[i]}'] = self.solution[i]

        dict_result = {"solution": dict}

        with open('../problem/solution.json', 'w') as json_file:
            json.dump([dict_result], json_file, indent=4)
