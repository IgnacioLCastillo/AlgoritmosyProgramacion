import numpy as np
import random
#from misLibrerias import myMatrixLibrary

def miMatriz_Carga(pMartiz):
    for i in range(0,3):
        for j in range(0,3):
            while True:
                try:
                    pMartiz[i][j] = int(input(f"Ingrese Valor {i}{j}: "))
                except ValueError:
                    print("Error, Ingrese un numero")
                    continue
                if pMartiz[i][j] <= 0 or pMartiz[i][j] >=10:
                    print("Debes escribir un en rango 0 a 10.")
                    continue
                break
def miMatri_CargaAleatoria(pMartiz):
    for i in range(0,3):
        for j in range(0,3):
            pMartiz[i][j] = np.random.randint(1,10)

def miMatriz_Muestra(pMartiz):
    for i in range(0,3):
        print('\n')
        for j in range(0,3):
            print(f"{pMartiz[i][j]}",end=' | ')

def miMatriz_Diagonal(pMartiz):
    for i in range(0,3):
        for j in range(0,3):
            if i == j:
                print(f"Valor {i},{j}:{pMartiz[i][j]}")

def miMatriz_DebajoDiagonalppal(pMartiz):
    for i in range(0,3):
        for j in range(0,3):
            if i>=j:
                print(f"Valor {i},{j}:{pMartiz[i][j]}")

def miMatriz_MaximoEncimaDiagonalppal(pMartiz):
    primerMax=False
    for i in range(0,3):
        for j in range(0,3):
            if i<=j:
                if primerMax==False:
                    miMaximo = pMartiz[i][j]
                    primerMax=True
                elif pMartiz[i][j] > miMaximo:
                    miMaximo = pMartiz[i][j]
    return miMaximo


def miMatriz_MinimoBajoContraDiagonal(pMartiz):
    primerMin=False
    for i in range(0,3):
        for j in range(0,3):
            if i+j>=2:
                if primerMin==False:
                    miMinimo = pMartiz[i][j]
                    primerMin=True
                elif pMartiz[i][j] < miMinimo:
                        miMinimo = pMartiz[i][j]
    return miMinimo



def miMenu():
    print("\nMenu de Opciones\n")
    print("1. Cargar Matriz Manualmente")
    print("2. Cargar Matriz Aleatoriamente")
    print("3. Mostrar Matriz")
    print("4. Mostrar Diagonal Principal")
    print("5. Mostrar Debajo de la Diagonal Principal")
    print("6. Maximo Encima de la Diagonal Principal")
    print("7. Minimo Debajo de la Contra Diagonal")
    print("8. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def mimain():
    miMatrix = np.zeros(shape=(3, 3), dtype=int)
    #filas = len(miMatrix)
    #columnas = len(miMatrix[0])
    while True:
        opcion = miMenu()
        if opcion == 1:
            miMatriz_Carga(miMatrix)
            #myMatrixLibrary.cargaMatriz(miMatrix, filas, columnas)
        elif opcion == 2:
            miMatri_CargaAleatoria(miMatrix)
            miMatriz_Muestra(miMatrix)
        elif opcion == 3:
            miMatriz_Muestra(miMatrix)
        elif opcion == 4:
            miMatriz_Muestra(miMatrix)
            miMatriz_Diagonal(miMatrix)
        elif opcion == 5:
            miMatriz_Muestra(miMatrix)
            miMatriz_DebajoDiagonalppal(miMatrix)
        elif opcion == 6:
            print(f"El maximo encima de la diagonal principal es: {miMatriz_MaximoEncimaDiagonalppal(miMatrix)}")
        elif opcion == 7:
            print(f"El minimo debajo de la contra diagonal es: {miMatriz_MinimoBajoContraDiagonal(miMatrix)}")
        elif opcion == 8:
            break
        else:
            print("Opcion no valida")


    #print(miMatrix)

########AREA PUBLICA#####|
mimain()