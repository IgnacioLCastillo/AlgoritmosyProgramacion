# -*- coding: utf-8 -*-
''''#Forma clásica de crear un archivo:

f = open("archivotext.txt", "w") #Creamos el archivo
f.write("Creando archivo de texto en python de forma clásica") #<-Escribimos en el
f.close() #Cerramos el archivo
'''

#Utilizando With As <-----------------------Nuestra forma de hacerlo
with open ("archivotext.txt", "w") as f: #Creamos el archivo
    f.write("Creando archivo de texto en python usando whit as") #<-Escribimos en el
    print(f.name)
    #f.close()## No hace Falta

