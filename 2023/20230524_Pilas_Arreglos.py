# -*- coding: utf-8 -*-
import numpy as np

def Push(pPila, pdato, pTope):
    pTope = pTope + 1
    pPila[pTope] = pdato
    return pTope

def Pilallena(pTope,pElemMax):
    if pTope == pElemMax - 1:
        return True
    else:
        return False

def Pilavacia(pTope):
    if pTope == -1:
        return True
    else:
        return False

def Pop(Pila, pTope):
    pdato=Pila[pTope]
    pTope -= 1
    print("El número", pdato, "se ha sacado de la pila\n")
    return pTope

def ConsultarPila(Pila, Ptope):
    print("\nValores dentro de la pila:\n")
    for i in range(Ptope,-1,-1):
        txtnumero=str(Pila[i])
        print('|',txtnumero.zfill(3),'|','<--- PosicActual:',i, 'de',Ptope)
        print('________')
    print("\n")



def main():
    TamPila = int(input("Ingrese el tamaño de la Pila:"))
    top = -1
    Pila = np.zeros(shape=(TamPila), dtype=int)
    opcion=0
    while opcion < 4:
        print("Programa de Pilas con Vectores")
        print("1-Apilar (push)")
        print("2-DesApilar (pop)")
        print("3-Consultar")
        print("4-Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if Pilallena(top,TamPila) == True:
                print("Ha ocurrido un desbordamiento en la pila")
                input("Presione Enter para continuar...")
            else:
                print("Ingreso valor:")
                valor = int(input())
                top=Push(Pila, valor, top,)
        elif opcion == 2:
            if Pilavacia(top) == True:
                print("La pila está vacía")
                input("Presione Enter para continuar...")
            else:
                top=Pop(Pila, top)
        elif opcion == 3:
            if Pilavacia(top) == True:
                print("La pila está vacía")
            else:
                ConsultarPila(Pila, top)
            input("Presione Enter para continuar...")


main()