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


    """Análise se a solução já foi encontrada"""
    def sair(self, table):

        if table[len(table)-1:].min() >= 0:
            return True
        else: 
            return False
