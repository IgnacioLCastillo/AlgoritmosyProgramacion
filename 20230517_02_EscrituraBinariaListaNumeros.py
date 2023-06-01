# -*- coding: utf-8 -*-
with open("MisNumeros.bin", "wb") as archivo:
    milista=[1,2,3,4,6,8]
    listatransformadaabyte=bytearray(milista)
    archivo.write(listatransformadaabyte)


#En Python, la función list() puede recibir un objeto de tipo bytes o bytearray y transformarlo en una lista de enteros.
#Esto es posible debido a que los objetos de tipo bytes y bytearray representan una secuencia de bytes,
# donde cada byte se puede interpretar como un entero en el rango de 0 a 255.
#datos = b'\x01\x02\x03\x04\x06\x08'
#lista = list(datos)
#print(lista)  # [1, 2, 3, 4, 6, 8]

with open("MisNumeros.bin", "rb") as archivo:
    milista = list(archivo.read())

print(milista)

