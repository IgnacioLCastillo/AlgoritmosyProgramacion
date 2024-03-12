# Abrir el archivo de texto
with open('Mitexto.txt', 'r') as archivo:
    contenido = archivo.read()

# Inicializar el contador
contador = 0

# Recorrer el contenido del archivo
for letra in contenido:
    # Convertir la letra a minuscula para simplificar la comparacion
    letra = letra.lower()
    print(letra,end="")
    # Verificar si la letra es una vocal
    if letra in ['a', 'e', 'i', 'o', 'u']:
        contador += 1

# Imprimir el resultado
print('\nCantidad de vocales en el archivo:', contador)