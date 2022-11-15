import numpy as np

def CreateListVariableController(nLim, nCol):
    nCol =  int(nCol)
    nLin =  int(nLim)

    listVariables = np.zeros((nLin, nCol))
    
    print(listVariables)
    return listVariables