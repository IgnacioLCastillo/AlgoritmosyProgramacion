# -*- coding: utf-8 -*-
'''La venta de un negocio se carga en una matriz de 3X3. El propietario dividió a la matriz en tres partes.
La parte superior corresponde a la venta del empleado 1 (Amarilla), la diagonal principal la venta del empleado 2 (Roja) y la parte inferior de la diagonal al empleado 3 (Rosa).
Se pide:
a) Cargar la matriz con valores enteros que van del 0 al 9. En caso de cargar datos fuera del rango informar error y volver a intentarlo.
b) Informar el promedio vendido del Empleado 1 y 2
c) Informar la cantidad de productos vendidos con precio entre 6 y 9.
d) Aprovechamos y transponemos la matriz.
Ejemplo
Según ejemplo el resultado seria.
Promedio de Vendedor 1 y 2 --> 30/ 6 = 5
Cantidad de Productos vendido entre 6 y 9= 4 producto.
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
                if pmatriz[i][j] < 0 or pmatriz[i][j] > 9:
                    print("Error. El valor ingresado debe estar entre 0 y 9.")
                    continue
                else:
                    break

def udfPromedioVendedor1y2(pmatriz,pfila,pcolumna):
    suma = 0
    cont = 0
    for i in range(0,pfila,1):
        for j in range(0,pcolumna,1):
            if i <= j:
                suma += pmatriz[i][j]
                cont += 1
    return suma, cont


def udfConteo6a9(pmatriz,pfila,pcolumna):
    cont = 0
    for i in range(0,pfila,1):
        for j in range(0,pcolumna,1):
            if pmatriz[i][j] >= 6 and pmatriz[i][j] <= 9:
                cont += 1
    return cont


def udfMiMain():
    tamFila = 3
    tamColumna = 3
    matriz = np.zeros(shape=(tamFila,tamColumna), dtype=int)
    udfCargarMatriz(matriz, tamFila, tamColumna)
    recSuma,recCant=udfPromedioVendedor1y2(matriz, tamFila, tamColumna)
    print ("El Promedio del venderdor 1 y 2 (Rojo y Amarillo) es: ",recSuma/recCant)
    resultadoConteo = udfConteo6a9(matriz, tamFila, tamColumna)
    print ("La cantidad de productos vendidos entre 6 y 9 es: ",resultadoConteo)
    print(matriz)

#MiMain- Publico
udfMiMain()