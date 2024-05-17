# -*- coding: utf-8 -*-
'''Dada la siguiente matriz de 3X3 deberá escribir en el código que implemente las funciones necesarias para :
a) Cargar a la Matriz solo mayores o iguales a 0. En caso de que asi no sea informar error y volver a intentar la carga
b) Sumar los números impares de la parte superior de la matriz incluyendo su diagonal principal.   (Área Gris)
c) Transponer la matriz. (Pasar Filas a Columnas)
'''
import numpy as np

def udfCargarMatriz(pmatriz,pfila,pcolumna):
    for i in range(0,pfila,1):
        for j in range(0,pcolumna,1):
            while True:
                try:
                    pmatriz[i][j] = int(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
                except ValueError:
                    print("Error. Debe ingresar un número entero.")
                    continue
                if pmatriz[i][j] <= 0:
                    print("Error. El valor ingresado debe ser mayor o igual a 0")
                    continue
                else:
                    break

def udfSumaImparSuperior(pmatriz,pfila,pcolumna):
    suma = 0
    cont = 0
    for i in range(0,pfila,1):
        for j in range(0,pcolumna,1):
            if pmatriz[i][j]%2 ==0:
                suma += pmatriz[i][j]
    return suma

def udTransponerMatriz(pmatriz,pfila,pcolumna):
    matrizTranspuesta = np.zeros(shape=(pcolumna,pfila), dtype=int)
    for i in range(0,pfila,1):
        for j in range(0,pcolumna,1):
            matrizTranspuesta[j][i] = pmatriz[i][j]
    return matrizTranspuesta

def udfMiMain():
    tamFila = 3
    tamColumna = 3
    matriz = np.zeros(shape=(tamFila,tamColumna), dtype=int)
    udfCargarMatriz(matriz, tamFila, tamColumna)
    recSuma=udfSumaImparSuperior(matriz, tamFila, tamColumna)
    print(matriz)
    print ("La suma de la parte superior de la matriz es: ",recSuma)
    matrizTranspuesta = udTransponerMatriz(matriz, tamFila, tamColumna)
    print("Matriz Transpuesta")
    print(matrizTranspuesta)

#MiMain- Publico
udfMiMain()