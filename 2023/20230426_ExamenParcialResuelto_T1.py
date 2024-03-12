import numpy as np

def cargaDeMatriz(matriz, fil, col):
    for i in range(0, fil, 1):
        for j in range(0, col, 1):
            while True:
                try:
                    valor = int(input("Ingrese valor: "))
                except ValueError:
                    print("Error, Ingrese un numero")
                    continue
                if valor < 0:
                    print("Ingrese un numero positivo: ")
                    continue
                else:
                    break
            matriz[i][j] = valor

def sumaImpares(matriz, fil, col):
    suma = 0
    for i in range(0, fil, 1):
        for j in range(0, col, 1):
            if j>=i:
                if matriz[i][j] % 2 != 0:
                    suma += matriz[i][j]
    return suma

def transponer(matriz, fil, col):
    matriz2 = np.zeros([fil, col])
    for i in range(0, fil, 1):
        for j in range(0, col, 1):
            matriz2[i][j] = matriz[j][i]
    return matriz2

filas = 3
columnas = 3
matriz = np.zeros([filas, columnas])



cargaDeMatriz(matriz, filas, columnas)
print(matriz)
print("Sumatoria de impares de la parte superior de la matriz incluyendo su diagonal principal: ", sumaImpares(matriz, filas, columnas))
print("Matriz transpuesta : \n",transponer(matriz, filas, columnas))