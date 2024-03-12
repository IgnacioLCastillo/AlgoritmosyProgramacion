## La lista de nombres a escribir
nombres = ["Juan", "Susana", "Andrea", "Melanie", "Andrés"]

## Abrimos en modo escritura
archivo = open("c:nombres.txt", "w")

## Recorremos la lista y agregamos cada nombre al archivo
for nombre in nombres:
    archivo.write(nombre + "\n")
    print(nombre, file=archivo)

## Muy importante cerrar el archivo.
archivo.close()

contenido = open("nombres.txt", "r")

## Recorremos y mostramos cada línea enumerada
contador = 1
for línea in contenido:
    print("Línea", contador, ":", línea)
    contador += 1

archivo.close()