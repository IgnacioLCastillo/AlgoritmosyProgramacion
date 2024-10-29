# -*- coding: utf-8 -*-
'''

print('Abro archivo')
miArchivo = open('nombres.txt','r')
micontenido=miArchivo.read()
print('Contenido:',micontenido)
'''

'''
#Ejemplo de lectura de archivos en Python - Caso 1 Apertura
print('-------------Metodo Apertura y lectura Simple------------------')
print('Abro archivo')
miArchivo = open('nombres.txt','r')
print('Cierro Archivo')
miArchivo.close()
'''
#-------------------------------------------------------------------------------
'''
#Ejemplo de lectura de archivos en Python - Caso 2 Apertura y lectura Por linea
print('-------------Metodo Apertura Capturando exceptions------------------')
try:
    print("Abierto con Exito")
    archivo =  open("Carta_Texto.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
#except FileNotFoundError:
#    print("El archivo no se encuentra en la ruta especificada.")
except Exception as Otromensaje:
    print("Ocurrio un error al abrir el archivo:", Otromensaje)
'''
#-------------------------------------------------------------------------------
'''
print('-------------Metodo Apertura y lectura Simple------------------')
#Hace la lectura hasta que encuentra un salto de linea
miArchivo = open('Carta_Texto.txt','r')
print('datos:',miArchivo)
for linea in miArchivo:
    print('linea:',linea)
miArchivo.close()
'''

#-------------------------------------------------------------------------------
'''
#Ejemplo de lectura de archivos en Python - Caso 3 Apertura y lectura
print('-------------Recorrer el contenido del archivo letra por letra------------------')
with open('Mitexto.txt', 'r') as archivo:
    contenido = archivo.read()
for letra in contenido:
        print (letra,end="*")
'''
#-------------------------------------------------------------------------------
'''
#Ejemplo de lectura de archivos en Python - Caso 4 Apertura y lectura
print('-------------Con ReadLine (UNA LINEA) Iterando con un While------------------')
with open("nombres.txt", "r") as archivo:
    print(archivo)
    print(archivo.tell())
    linea = archivo.readline()
    print(archivo.tell())
    while linea:
        print(linea)
        linea = archivo.readline()
        print('-------------Muestro cada vez que se desplaza------------------')
        print(archivo.tell())
        print('-------------Muestro el contenido de la linea------------------')
'''
#-------------------------------------------------------------------------------
''' 
#Ejemplo de lectura de archivos en Python - Caso 5 Apertura y lectura
print('-------------Con ReadLines (TODAS LAS LINEAS) Iterando con un For------------------')
with open("nombres.txt", "r") as archivo:
    todaslineas = archivo.readlines()
    print('Todas',todaslineas)
    for cadaLinea in todaslineas:
        print(cadaLinea)
        print(archivo.tell()) #me devuelve el puntero de lectura que quedo anclado a fin de archivo porque
        #

'''
#-------------------------------------------------------------------------------
'''
#Ejemplo de lectura de archivos en Python - Caso 6 Apertura y lectura
print('-------------Con Read todas las lineas. Luego separo las palabras------------------')
cantidadpalabras=0
with open('nombres.txt', 'r') as archivo:
    todaslineas = archivo.readlines() # Separamos el contenido del archivo en lineas
    print(todaslineas)
    for cadaLinea in todaslineas:  # Iteramos a traves de las lineas
       print(cadaLinea)
       palabras = cadaLinea.split()  # Dividimos la linea en palabras
       print(palabras,len(palabras))
       cantidadpalabras+=len(palabras)
       #otrocontadorA=0
       #for palabra in palabras:
            #primera letra
       #     if palabra[0].upper()=='A':
       #         otrocontadorA+=1
       #print("Letras A:",otrocontadorA)
     #Solo lo pusimos para ver cuantas palabras hay en el archivo y detectar las que empezaban con A
print('total de palabras leidas',cantidadpalabras)
'''
#-------------------------------------------------------------------------------
'''
#Ejemplo de lectura de archivos en Python - Caso 7 Apertura y lectura
print('-------------Con Read Mostrado todo el contenido. Luegi el Tell------------------')
with open('nombres.txt', 'r') as archivo:
    contenido = archivo.read()  # Levantamos_todo el contenido
    print(contenido)
    print('Bytes recorridos luego de hacer el read() que se come todo el file',archivo.tell())
    print('-------------Con Read Mostrado todo el contenido solo 3 cacarteres. Luego el Tell------------------')
    archivo.seek(0) #Me posiciono en el inicio porque cuando hago read voy al final.
    # Impprimo laposicion actual
    contenido = archivo.read(3)
    print('Bytes recorrido luedo de comer solo 3 caracteres',archivo.tell())
    print(contenido)
'''

#-------------------------------------------------------------------------------

archivo = open("archivo.txt", "r")
contenido = archivo.read(10)  # Leer los primeros 10 caracteres
print(contenido)
archivo.seek(0)  # Volver al inicio del archivo
''' Leer todo el contenido desde el inicio'''
contenido_completo = archivo.read()
print(contenido_completo)
archivo.close()
