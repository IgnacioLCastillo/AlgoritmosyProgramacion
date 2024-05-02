# -*- coding: utf-8 -*-
'''
Exception: Es la clase base para todas las excepciones incorporadas en Python. Capturar esta excepción manejará cualquier tipo de excepción.
TypeError: Se produce cuando se realiza una operación inapropiada para el tipo de datos específico.
ValueError: Se produce cuando se recibe un argumento con el tipo correcto pero un valor incorrecto.
ZeroDivisionError: Se produce cuando intentas dividir por cero.
IndexError: Se produce cuando intentas acceder a un índice fuera del rango de una secuencia.
KeyError: Se produce cuando intentas acceder a una clave que no está presente en un diccionario.
FileNotFoundError: Se produce cuando intentas abrir un archivo que no existe.
IOError: Se produce cuando ocurre un error de entrada/salida, como por ejemplo cuando un archivo no se puede abrir o leer.
NameError:  Es útil para detectar errores de sintaxis o errores de programación relacionados con la definición y el alcance de los nombres y variables en tu código Python.
'''
'''
#Caso 1
try:
    suma=suma+2
#except NameError:  # Variable desconocida
#        print("Variable Desconocida")
except Exception as mierrorcapturado:
        print("Error:",mierrorcapturado)
'''
#Caso 2
'''
try:
    1/0
#except ZeroDivisionError:  # Error en Division
#        print("Error Division por cero")
except Exception as mierrorcapturado:
        print("Error:",mierrorcapturado)
'''


#Caso 3 *hay que poner un char para que falle)
while True:
    try:
        viValor=int(input("Ingrese Valor"))
    except ValueError:  # Variable desconocida
            print("Error. Debe ingresar un Entero")
            continue
    if viValor < 0:
        print("Debes escribir un numero positivo.")
        continue
    break

