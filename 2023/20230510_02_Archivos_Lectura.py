# -*- coding: utf-8 -*-

'''
print('-------------Metodo Apertura y lectura Simple------------------')
print('Abro archivo')
miArchivo = open('nombres.txt','r')
print('Cierro Archivo')
miArchivo.close()


print('-------------Metodo Apertura Capturando exceptions------------------')
try:
    print("Abierto con Exito")
    archivo =  open("mi_archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")
except Exception as Otromensaje:
    print("Ocurrio un error al abrir el archivo:", Otromensaje)

print('-------------Metodo Apertura y lectura Simple------------------')
miArchivo = open('nombres.txt','r')
for linea in miArchivo:
    print(linea)

miArchivo.close()

print('-------------Recorrer el contenido del archivo letra por letra------------------')
with open('Mitexto.txt', 'r') as archivo:
    contenido = archivo.read()
for letra in contenido:
    print (letra,end="")



print('-------------Con ReadLine (UNA LINEA) Iterando con un While------------------')
with open("nombres.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(linea)
        linea = archivo.readline()
        print('-------------Muestro cada vez que se desplaza------------------')
        print(archivo.tell())


print('-------------Con ReadLines (TODAS LAS LINEAS) Iterando con un For------------------')
with open("nombres.txt", "r") as archivo:
    todaslineas = archivo.readlines()
    print('Todas',todaslineas)
    for cadaLinea in todaslineas:
        print(cadaLinea)
        print(archivo.tell())


print('-------------Con Read todas las lineas. Luego separo las palabras------------------')
cantidadpalabras=0
with open('nombres.txt', 'r') as archivo:
    todaslineas = archivo.readlines() # Separamos el contenido del archivo en lineas
    print(todaslineas)
    for cadaLinea in todaslineas:  # Iteramos a traves de las lineas
        palabras = cadaLinea.split()  # Dividimos la linea en palabras
        print(palabras,len(palabras))
        cantidadpalabras+=len(palabras)
print('total de palabras leidas',cantidadpalabras)


print('-------------Con Read Mostrado todo el contenido. Luegi el Tell------------------')
with open('nombres.txt', 'r') as archivo:
    contenido = archivo.read()  # Levantamos_todo el contenido
    print(contenido)

    print('-------------Con Read Mostrado todo el contenido solo 3 cacarteres. Luego el Tell------------------')
    archivo.seek(0) #Me posiciono en el inicio porque cuando hago read voy al final.
    # Impprimo laposicion actual
    contenido = archivo.read(3)
    print(archivo.tell())
    print(contenido)

'''

