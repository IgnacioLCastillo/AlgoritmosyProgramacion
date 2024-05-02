#Definicion y dimensionamiento
import array as arr

""" Esta implementación de Factorial es una forma de resolverlo
No es la mejor...más adelante en la materia vamos a ver otra
"""

def udfCuentaRegresivaTradicional (pnumero):
    for i in (range(pnumero,0,-1)):
        print (i)
''' Seria como hacer....desde 10, hasta 1, bajando 1 en 1'''

def udfCuentaRegresivaRecursiva(pnumero):
    print (pnumero)
    if pnumero==1: #Caso Base
        return 1
    else:
        return udfCuentaRegresivaRecursiva(pnumero-1)

def udfCuentaRegresivaRecursivaInversa(pnumero,ptope):
    if pnumero == ptope:  # Caso Base
        print(pnumero)
        return ptope
    else:
        print(pnumero)
        return udfCuentaRegresivaRecursivaInversa(pnumero + 1, ptope)


'''
5 (5-1)
4 (4-1)
3 (3-1)
2 (2-1)
1 (1)
'''

def udfCargaVectorconRecursividad(parreglo,pnumero):
    parreglo[pnumero] = int(input(f"Ingrese un valor en la posicion {pnumero}"))
    if pnumero==0:
        return -1
    else:
        return udfCargaVectorconRecursividad(parreglo,pnumero-1)

def udfMostrarVectorconrecursividad(parreglo,pnumero):
    print(parreglo[pnumero],end='|')
    if pnumero==0:
        return -1
    else:
        return udfMostrarVectorconrecursividad(parreglo,pnumero-1)


def SumaRecursiva(numero):
    if (numero == 1):
        return  1
    else:
        resul=numero + SumaRecursiva(numero-1)
        print(resul)
        return resul


def miFactorial(numero):
    if (numero == 0) or (numero == 1): #Caso Base
        return 1
    else:
        valor=numero*miFactorial(numero-1)
        #print(valor)
        return valor

def miFactorialtradicional(numero):
    if (numero == 0) or (numero == 1):
        return 1
    for i in range(1,numero,1):
        numero=numero*i

    return numero


#mifactorial(5)   5*(4*3*2*1) -- 5-4! Factorial de 4 (la cantidad de combinaciones)
#5*mifactorial(4) 4*(3*2*1)
#4*mifactorial(3) 3*(2*1)
#3*mifactorial(2) 2*1
#2*mifactorial(1) *1
#1



'''***************************Seccion del Programa Principal******************************'''


def miMain():
    miArreglo = arr.array('i',range(5))
    cantElem= len(miArreglo)

    viOpcion=-1 #Global
    while viOpcion!=7:
        print('\n')
        print('1-Conteo Tradicional')
        print('2-Conteo Recursivo')
        print('3-Suma Recusiva')
        print('4-Factorial Recursivo/Sin Recursividad')
        print('5-Carga Vector con recusividad')
        print('6-Mostrar Vector con Recursividad')
        print('7-Salir')
        viOpcion=int(input("Seleccione:"))

        if viOpcion==1:
            n = int(input("Numero:"))
            udfCuentaRegresivaTradicional(n)
        elif viOpcion == 2:
            n = int(input("Numero:"))
            print("---Descendente---")
            udfCuentaRegresivaRecursiva (n)
            print("---Ascendente---")
            udfCuentaRegresivaRecursivaInversa(n-(n-1),n)
        elif viOpcion == 3:
            n = int(input("Numero:"))
            print(SumaRecursiva(n))
        elif viOpcion == 4:
            n = int(input("Numero:"))
            print('Factorial Recursivo:',miFactorial(n))
            print('Factorial Iterando:',miFactorialtradicional(n))
        elif viOpcion == 5:
            udfCargaVectorconRecursividad(miArreglo, cantElem - 1)
        elif viOpcion == 6:
            udfMostrarVectorconrecursividad(miArreglo, cantElem - 1)
        else:
            print ('Error')



#*-*-*-*-*-*-*-* AREA GLOBAL
miMain()





#print(miFactorial(n))
#print(miFactorialtradicional(n))

'''



""" Para jugar un rato......
Python tiene una librería para graficar que se llama 
MatPlotLib
referencia: http://www.iac.es/sieinvens/python-course/source/matplotlib.html

Supongamos que queremos graficar el factorial de una serie de números...

Acá va el ejemplo:

"""

# importar el módulo pyplot
import matplotlib.pyplot as plt
# vamos a poner puntos del gráfico primero, cada punto del eje X es un número
# el eje Y será el factorial de se punto X

# esta instrucción arma una figura donde se van a graficar los puntos
plt.figure()

""" prueben cambiar la cantidad de puntos y vean qué pasa.
No usar números muy grandes porque el factorial se dispara !!! y como es un
gráfico simple las escalas quedan mal...
es para que vean otras cosas....
"""

cantidadDePuntos = 4
for x in range(cantidadDePuntos + 1):
    # función factorial (que la definimos arriba)
    y = factorial(x)
    # ahora le decimos a la librería que vaya graficando puntos
    plt.plot(x, y, 'rs')


'''