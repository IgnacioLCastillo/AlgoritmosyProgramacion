#Definicion y dimensionamiento
import array as arr

""" Esta implementación de Factorial es una forma de resolverlo
No es la mejor...más adelante en la materia vamos a ver otra
"""

def udfCuenta_descendete_Tradicional (pnumero):
    for i in (range(pnumero,0,-1)):
        print (i)
''' Seria como hacer....desde 10, hasta 1, bajando 1 en 1'''

def udf_Cuenta_descendente_recursiva(pnumero):
s
    if pnumero==1: #Caso Base
        return 33
    else:
        #Si dejo el return es porqueu del lado del main quiero recibir el un valor.
        #Aca dejo el 33 pero es un absurdo. Podria haber dejado solo return y ya porque
        #solo queria cortar la recursividad mediante el caso base.
        #si dejo 33 y esto se muestra en el main, es porque el 33 es el retorno de la funcion cuando llega a 1
        #el 33 se lo pasa a la funcion que lo llamo que es 2. Y asi sucesivamente. La ultima que se ejecuta es
        #el 5. El 5 hace un return aqui y muestra el 33 que fue el valor que se fueron pasando
        #todas las llamadas intermedias.
        #En este caso no tiene sentido el 33. Pero si lo tuviera, se lo pasaria a la funcion que lo llamo
        #Si dejaba como estaba antes sin retotno contaria igual pero cuando quiero hacer el print en el main
        #me retorna none y eso es porque corto con 33 la funcion que llego a 1 pero cuando ejecuta la 2
        #el 33 no se lo pasa porque no hay return y por eso muestra none.
        #udf_Cuenta_descendente_recursiva(pnumero - 1)
        return udf_Cuenta_descendente_recursiva(pnumero-1)

def udf_cuenta_ascendente_recursiva(pnumero,ptope):
    if pnumero == ptope:  # Caso Base
        print(pnumero)
        return
    else:
        print(pnumero)
        #udf_cuenta_ascendente_recursiva(pnumero + 1, ptope)
        return udf_cuenta_ascendente_recursiva(pnumero + 1, ptope)

def udfCuentaRegresivaRecursivaInversa_Ascendente(pnumero, ptope):
    if pnumero > ptope:  # Caso base, cuando pnumero supera el tope
        return
    print(pnumero)
    udfCuentaRegresivaRecursivaInversa_Ascendente(pnumero + 1, ptope)

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
    while viOpcion!=8:
        print('\n')
        print('1-Conteo Descendente Tradicional')
        print('2-Conteo Descendente Recursivo')
        print('3-Conteo Ascendente Recursivo')
        print('4-Suma Recusiva')
        print('5-Factorial Recursivo/Sin Recursividad')
        print('6-Carga Vector con recusividad')
        print('7-Mostrar Vector con Recursividad')
        print('8-Salir')
        viOpcion=int(input("Seleccione:"))

        if viOpcion==1:
            n = int(input("Numero:"))
            udfCuenta_descendete_Tradicional(n)
        elif viOpcion == 2:
            n = int(input("Numero:"))
            print("---Descendente---")
            print(udf_Cuenta_descendente_recursiva(n))
        elif viOpcion == 3:
            n = int(input("Numero:"))
            print("---Ascendente---")
            udf_cuenta_ascendente_recursiva(n-(n-1),n)
        elif viOpcion == 4:
            n = int(input("Numero:"))
            print(SumaRecursiva(n))
        elif viOpcion == 5:
            n = int(input("Numero:"))
            print('Factorial Recursivo:',miFactorial(n))
            print('Factorial Iterando:',miFactorialtradicional(n))
        elif viOpcion == 6:
            udfCargaVectorconRecursividad(miArreglo, cantElem - 1)
        elif viOpcion == 7:
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