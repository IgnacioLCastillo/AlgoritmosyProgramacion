import numpy as np
from Algoritmos_y_Programacion.misLibrerias import myMatrixLibrary

#*---------------
miMatrix = np.zeros(shape=(2,3),dtype=int)
filas=len(miMatrix)
columnas=len(miMatrix[0])
print(miMatrix)
myMatrixLibrary.MostrarMatriz(miMatrix,filas,columnas)
myMatrixLibrary.cargaMatriz(miMatrix,filas,columnas)
myMatrixLibrary.MostrarMatriz(miMatrix,filas,columnas)

