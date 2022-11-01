import numpy as np

class Simplex:

    z = []                  #Função a ser maximizada/minimizada
    b = []                  #Lado direito das restrições
    num_var = 0             #Número de variáveis
    num_restr = 0           #Número de restrições
    maximize = True         #Verifica se é uma maximização ou minimização
    dual = False            #Verifica se a resolução é pelo dual ou primal
    restr = []              #restrições
    sinal= []               #Sinais das restrições: <=, >=, =
    table = []              #Tabela para execução do método simplex
    base = []               #Indice de X para os valores básicos
    Cb = []                 #Valores em Z das variáveis básicas
    artificial = False      #Avalia se exixte alguma variavel artificial para usar o método das duas fases
    base_init = 0           #Base inicial do problema para ser aplicado na segunda fase do problema
    arti_function = []      #Função das Variáveis artificiais
    novo_z = []             #Novo Z calculado para operração do método das duas fases
   

    '''Método construtor da Classe'''
    def __init__(self, z, b, num_var, num_restr, sinal, restr, maximize, dual):
        self.num_var = num_var
        self.num_restr = num_restr
        self.restr = restr
        self.sinal= sinal
        self.z = z
        self.b = b
        self.maximize = maximize
        self.dual = dual

    
    '''Análisa se a solução já foi encontrada'''
    def out(self, table):

        if table[len(table)-1:].min() >= 0:
            return True
        else: 
            return False


    '''Método que adiciona variaveis de folga, excesso e artificial'''
    def addVariables(self):

        self.table = np.matrix(self.restr, float)
        
        for i in range(0, len(self.restr)):
            
            #Adiciona variáveis: +artificial e -excesso
            if(self.sinal[i] == '>='):
                matr = np.zeros((self.num_restr, 2))
                matr[i,0] = -1
                matr[i][1] = 1
                self.artificial = True
                self.arti_function.append(0)
                self.arti_function.append(-1)
                self.Cb.append(-1)

            #Adiciona variáveis: +artificial
            elif(self.sinal[i] == '='):
                matr = np.zeros((self.num_restr, 1))
                matr[i,0] = 1
                self.artificial = True
                self.arti_function.append(-1)
                self.Cb.append(-1)

                
            #Adiciona variáveis: +folga
            elif(self.sinal[i] == '<='):
                matr = np.zeros((self.num_restr, 1))
                matr[i,0] = 1
                self.Cb.append(0)
           
            self.table = np.concatenate(([self.table, matr]), axis=1)
            self.base.append(self.table.shape[1])
    
  
    '''Oraganiza a função a ser otimizada'''
    def functionObjetivo(self):
        
        for i in range (0, self.table.shape[1]-len(self.z)):
                self.z.append(0)
        
        '''Organiza a função objetivo caso exista variáveis artificiais'''
        if self.artificial == True:
              
            for i in range (0, self.num_var):
                self.arti_function = [0] + self.arti_function

            self.arti_function.append(0)

            for i in range(0, self.table.shape[1]):
                soma = 0
                for j in range(0, len(self.table)):
                    soma = soma + self.Cb[j]*self.table[j, i]                                   
                
                soma = soma - self.arti_function[i]
                self.novo_z.append(soma)
        else:
            self.novo_z = np.array(self.z)*-1
   
    
    '''Fase II - Atualiza a função objetivo'''
    def functionObjetivo1(self):

            for i in range(0, self.table.shape[1]):
                soma = 0
                for j in range(0, len(self.Cb)):
                    soma = soma + self.Cb[j]*self.table[j, i]                                          
                soma = soma - self.z[i]
                self.table[len(self.table)-1, i] = soma
           
   
    '''Organiza a tabela para aplicação do método simplex'''
    def organizeTable(self):

        self.addVariables()
        self.table = np.hstack([self.table, self.b])
        self.functionObjetivo()
        self.table = np.vstack([self.table, self.novo_z])

        '''Para o passo II - elimina coluna das variáveis artificiais (Caso resrição >= ou =)'''
        self.base_init = sorted(self.base)

    
    def basicsVariables(self, posPivo):
        '''A base ainda não está muito bem definida, atualizarei depois'''
        self.base[posPivo[0]] = posPivo[1]+1
        self.Cb[posPivo[0]] = self.z[posPivo[1]]
        print('Base: ', self.base) 
        print('Cb', self.Cb)   


    '''Método de resolução usando o simplex'''
    def sem(self):

        self.organizeTable()
        
        '''Se existir variáveis artificiais resolvemos usando o método das duas fases'''
        if self.artificial == True:
            
            '''Enquanto Z diferente de 0'''   
            while self.table[self.table.shape[0]-1, self.table.shape[1]-1] != 0:
                self.solveSimplex()
                print(np.round(self.table, decimals=3))
            
            '''Apaga as colunas das variáveis artificiais para aplicar a 2 fase'''
            for i in range(0, len(self.base_init)):
                self.table = np.delete(self.table, self.base_init[i]-i-1, axis = 1)
                print('Nova tabela\n', np.round(self.table, decimals=3))

            '''Fase II'''
            self.functionObjetivo1()
            print(np.round(self.table, decimals=3),'\n')

        while self.out(self.table) == False:
            self.solveSimplex()
            print(np.round(self.table, decimals=3))


    '''Método de resolução usando o simplex'''
    def solveSimplex(self):

            """Posição do pivô"""
            posPivo = []
            list = []
            
            for i in range(0, len(self.table)-1): 
                """leva em consideração que esta operação só será realizada quando Pj superior a 0."""
                """Procura a coluna com o número mais negativo. Após isso, procura o menor valor positivo para a divisão entre o b (termo independente) e a coluna selecionada anteriormente"""
                if self.table[i, np.where(self.table[len(self.table)-1:,0:-1] == self.table[len(self.table)-1:,0:-1].min())[1][0]] > 0:
                    try:
                        list.append(self.table[i, self.table.shape[1]-1]/self.table[i, np.where(self.table[len(self.table)-1:,0:-1] == self.table[len(self.table)-1:,0:-1].min())[1][0]])

                    except:
                        print("Erro no Pivo")
                else:
                    list.append(100000000)

            posPivo.append(list.index(min(list)))
            posPivo.append(np.where(self.table[len(self.table)-1:,0:-1] == self.table[len(self.table)-1:,0:-1].min())[1][0])
            
            '''Atualiza as variaveis da base'''
            self.basicsVariables(posPivo)

            pivo = self.table[posPivo[0],posPivo[1]]
            print('Pivo:', pivo)

            if pivo != 0:
                '''Realiza o manipulação das linhas'''
                for i in range(0, len(self.table)):

                    mult = -float(self.table[i,posPivo[1]])/float(pivo)

                    for j in range(0, self.table.shape[1]):                                                                    
                        if i == posPivo[0]:
                            continue         
                        if i == len(self.table)-1:
                            self.table[i,j] = mult*self.table[posPivo[0], j] + self.table[i, j]
                            self.table[posPivo[0],j] = self.table[posPivo[0],j]/pivo
                        else:
                            self.table[i,j] = mult*self.table[posPivo[0], j] + self.table[i, j]
            else: 
                '''Pivo é igual a zero'''
                print('Erro 2')