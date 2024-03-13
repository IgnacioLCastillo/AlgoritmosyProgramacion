import numpy as np


def miMatriz_Carga(mipmatriz):
    for i in range(0,3):
        for j in range(0,3):
            mipmatriz[i][j] = int(input("Ingrese Valor:"))


def mimain():
    miMatrix = np.zeros(shape=(3, 3), dtype=int)
    filas = len(miMatrix)
    columnas = len(miMatrix[0])
    print(miMatrix)


mimain()