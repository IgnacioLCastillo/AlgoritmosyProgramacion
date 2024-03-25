import numpy as np


def miMatriz_Carga(pMartiz):
    for i in range(0,3):
        for j in range(0,3):
            pMartiz[i][j] = int(input(f"Ingrese Valor {i}{j}: "))


def mimain():
    miMatrix = np.zeros(shape=(3, 3), dtype=int)
    a= np.ones(shape=(3,3),dtype=int)
    miMatrixC = np.zeros(shape=(3, 3), dtype=int)
    filas = len(miMatrix)
    columnas = len(miMatrix[0])
    miMatriz_Carga(miMatrix)
    miMatriz_Carga(a)
    miMatriz_Carga(miMatrixC)
    print(miMatrix)
    print(a)
    print(miMatrixC)


mimain()