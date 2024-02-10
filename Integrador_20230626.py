# -*- coding: utf-8 -*
#Desarrollar un algorimo en python que lea un archivo de texto que se encuentra en su carpeta c:\pyfiles. El archivo se llama listadedeseos.txt
#Deberá leer el archivo validando que pueda abrise y que exista la ruta.
#Una vez que el archivo se abre deberan leer el archivo contabilizando la cantidad de palabras que hay por linea.
#Una vez que contabilizan deberan informar por pantalla la cantidad de palabras por linea.
#Ejemplo Salida.
#Viajar por todo el mundo y conocer diferentes culturas y lugares fascinantes.
#Linea 1 -> 12 palabras
#Aprender a tocar el piano y componer mis propias canciones.
#Linea 2 -> 10 palabras
print('-------------Con Read todas las lineas. Luego separo las palabras------------------')
cantidadpalabras=0
with open(r'c:\pyfiles\listadedeseos.txt', 'r', encoding="utf-8") as archivo:
    todaslineas = archivo.readlines() # Separamos el contenido del archivo en lineas
    print(todaslineas)
    for cadaLinea in todaslineas:  # Iteramos a traves de las lineas
        palabras = cadaLinea.split()  # Dividimos la linea en palabras
        print(palabras,len(palabras))
        cantidadpalabras+=len(palabras)
print('total de palabras leidas',cantidadpalabras)