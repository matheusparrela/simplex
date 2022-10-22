import numpy as np
import pandas as pd


class Simplex:
    function = 0
    variable = 0
    num_var = 0
    restrictions = []
    num_restr = 0
    maximize = True
    primal = True

    '''Método construtor da Classe'''
    def __init__(self, function, variable, num_var, restrictions, num_restr, maximize, primal):
        self.function = function
        self.variable = variable
        self.num_var = num_var
        self.restrictions = restrictions
        self.num_restr = num_restr
        self.maximize = maximize
        self.primal = primal


    """Análisa se a solução já foi encontrada"""
    def sair(self, table):

        if table[len(table)-1:].min() >= 0:
            return True
        else: 
            return False

    """Organiza a tabela para aplicação do método simplex"""
    def organizeTable(self, restr, num_var, coef):
        
        bases = self.restr - self.num_var

        for i in range (0, bases):
            z.append(0)

        b.append(0)

        z = np.array(z)*-1
        b = np.matrix(b)
        id = np.identity(bases, int)
        x = np.concatenate((self.coef, id), axis=1)

        t = np.vstack([x, z])
    
        table = np.hstack([t, b.transpose()])
        table = table.astype(float)

        return table

    def solveSimplex(self, table):

        while self.sair(table) == False:

            """Posição do pivô"""
            posPivo = []
            list = []
            for i in range(0, len(table)-1): 
                list.append(table[i,6]/table[i, np.where(table == table[len(table)-1:].min())[1][0]])
        
            posPivo.append(list.index(min(list)))
            posPivo.append(np.where(table == table[len(table)-1:].min())[1][0])
            
            pivo = table[posPivo[0],posPivo[1]]

            '''Realiza o manipulação das linhas'''
            for i in range(0,len(table)):

                mult = -float(table[i,posPivo[1]])/float(pivo)

                for j in range(0, 7):
                                                                        
                    if i == posPivo[0]:
                        continue
                        
                    if i == len(table):
                        table[posPivo[0],j] = table[posPivo[0],j]/pivo

                    else:
                        table[i,j] = mult*table[posPivo[0], j] + table[i, j]

            print(np.round(table, decimals=2),"\n\n")

        return table

    '''Método que adiciona variaveis de folga, excesso e artificial'''
    def addVariaveis(coeficientes, sinal, restr):

        table = np.matrix(coeficientes, float)

        for i in range(0, len(coeficientes)):
            
            #Adiciona variáveis de +artificial e -excesso
            if(sinal[i] == '>='):
                    matr = np.zeros((restr, 2))
                    matr[i,0] = -1
                    matr[i][1] = 1
                    
            #Adiciona variáveis de +artificial
            elif(sinal[i] == '='):
                matr = np.zeros((restr, 1))
                matr[i,0] = 1
                
            #Adiciona variáveis de +folga
            elif(sinal[i] == '<='):
                matr = np.zeros((restr, 1))
                matr[i,0] = 1
        
            table = np.concatenate(([table, matr]), axis=1)

        return table