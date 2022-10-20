import numpy as np
import pandas as pd
import sympy as sy

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


    def dual():
        #Código do algoritmo dual

    
    def primal():
         #Código do algoritmo primal
