# -*- coding: utf-8 -*-
import numpy as np

def encolar(pcola, ptop, pnumdato):
    pcola[ptop] = pnumdato
    ptop += 1
    return (ptop)


def desencolar(vec, ptop):
    numeroSaliente = vec[0]
    for x in range(ptop):
        vec[x] = vec[x + 1]

    vec[ptop] = 0
    ptop-= 1
    print ("Desencola el: ",numeroSaliente)
    return (ptop)

def colallena(ptop, pFINCOLA):
    #if ptop > pFINCOLA - 1:
    if ptop == pFINCOLA :
        return True
    else:
        return False

def colavacia(ptop):
    #if ptop < 1:
    if ptop == 0:
        return True
    else:
        return False


def consultar(vec, ptop):
    for x in range(ptop):
        print(vec[x], end=" ")
    print()



def main():

    finCola=int(input("Ingrese el tamaño de la cola:"))
    arreglo = np.zeros(shape = (finCola+1), dtype=int)
    opcion = 0
    tope = 0

    while opcion < 4:
        print("Programa de Colas con Vectores")
        print("1-Encolar")
        print("2-Desencola")
        print("3-Consultar")
        print("4-Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if colallena(tope,finCola)== True:
                print("Cola Llena")
                input("Presione Enter para continuar...")
            else:
                print("Encolar un Valor")
                numdato = int(input())
                tope=encolar(arreglo, tope, numdato)
                consultar(arreglo, tope)
                input("Presione Enter para continuar...")
        elif opcion == 2:
            if colavacia(tope) == True:
                print("Cola Vacia")
            else:
                print("Efectuando desencolamiento...")
                tope=desencolar(arreglo, tope)
                consultar(arreglo, tope)
            input("Presione Enter para continuar...")
        elif opcion == 3:
            print("Consultar")
            if colavacia(tope) == True:
                print("Cola Vacia")
            else:
                consultar(arreglo, tope)
            input("Presione Enter para continuar...")
        elif opcion == 4:
            print("Salir...")
        else:
            print("Opción inválida")


main()