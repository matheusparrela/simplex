import numpy as np


class Simplex:

    z = []              #Função a ser maximizada/minimizada
    b = []              #Lado direito das restrições
    num_var = 0         #Número de variáveis
    num_restr = 0       #Número de restrições
    maximize = True     #Verifica se é uma maximização ou minimização
    restr = []          #restrições
    sinal= []           #Sinais das restrições: <=, >=, =
    table = []          #Tabela para execução do método simplex
   

    '''Método construtor da Classe'''
    def __init__(self, z, b, num_var, num_restr, sinal, restr, maximize):
        self.num_var = num_var
        self.num_restr = num_restr
        self.maximize = maximize
        self.restr = restr
        self.sinal= sinal
        self.z = z
        self.b = b


    """Análisa se a solução já foi encontrada"""
    def sair(self, table):

        if table[len(table)-1:].min() >= 0:
            return True
        else: 
            return False


    """Organiza a tabela para aplicação do método simplex"""
    def organizeTable(self):
        
        self.addVariaveis()

        for i in range (0, self.table.shape[1]-self.num_var):
            self.z.append(0)

        self.b.append(0)
        self.z = np.array(self.z, float)*-1
        self.b = np.matrix(self.b, float)

        self.table = np.vstack([self.table, self.z])
        self.table = np.hstack([self.table, self.b.transpose()])   
 

    '''Método de resolução usando o simplex'''
    def solveSimplex(self):

        self.organizeTable()

        while self.sair(self.table) == False:

            """Posição do pivô"""
            posPivo = []
            list = []
            for i in range(0, len(self.table)-1): 
                list.append(self.table[i,6]/self.table[i, np.where(self.table == self.table[len(self.table)-1:].min())[1][0]])
        
            posPivo.append(list.index(min(list)))
            posPivo.append(np.where(self.table == self.table[len(self.table)-1:].min())[1][0])
            
            pivo = self.table[posPivo[0],posPivo[1]]

            '''Realiza o manipulação das linhas'''
            for i in range(0,len(self.table)):

                mult = -float(self.table[i,posPivo[1]])/float(pivo)

                for j in range(0, 7):
                                                                        
                    if i == posPivo[0]:
                        continue
                        
                    if i == len(self.table)-1:
                        self.table[i,j] = mult*self.table[posPivo[0], j] + self.table[i, j]
                        self.table[posPivo[0],j] = self.table[posPivo[0],j]/pivo

                    else:
                        self.table[i,j] = mult*self.table[posPivo[0], j] + self.table[i, j]

        return self.table


    '''Método que adiciona variaveis de folga, excesso e artificial'''
    def addVariaveis(self):

        self.table = np.matrix(self.restr, float)

        for i in range(0, len(self.restr)):
            
            #Adiciona variáveis: +artificial e -excesso
            if(self.sinal[i] == '>='):
                    matr = np.zeros((self.num_restr, 2))
                    matr[i,0] = -1
                    matr[i][1] = 1
                    
            #Adiciona variáveis: +artificial
            elif(self.sinal[i] == '='):
                matr = np.zeros((self.num_restr, 1))
                matr[i,0] = 1
                
            #Adiciona variáveis: +folga
            elif(self.sinal[i] == '<='):
                matr = np.zeros((self.num_restr, 1))
                matr[i,0] = 1
        
            self.table = np.concatenate(([self.table, matr]), axis=1)