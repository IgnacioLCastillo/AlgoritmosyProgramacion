# -*- coding: utf-8 -*-

#Ver Ejemplo 01 para entender el encoding
#cadena_bytes = b'Campe\xc3\xb3n del mundo'  # \xe1 representa el carácter 'ó' en UTF-8
#print(cadena_bytes)  # b'Hola \xe1 mundo'
#print(cadena_bytes.decode("utf-8"))
#(\xc3\xb3)Es una representación en notación de escape de dos bytes utilizada en Python para representar el carácter "ó"
# en codificación UTF-8
#En UTF-8, los caracteres que no pertenecen al conjunto ASCII se codifican utilizando más de un byte.
# En este caso, la "ó" se codifica como los bytes \xc3 y \xb3.
#La notación de escape \x se utiliza en Python para representar un byte en hexadecimal.
# Por lo tanto, \xc3 representa el byte 0xC3 y \xb3 representa el byte 0xB3.
# En conjunto, \xc3\xb3 representa la secuencia de bytes que corresponde al carácter "ó" en UTF-8.

with open("Mitextobinario.bin", "wb") as archivo:
    texto=b"Argentina es tricampeon mundial.\n" #Aca lo paso a bit con el b
    archivo.write(texto)
    texto="pythön es tricampeón mundial." #Aca lo paso a bit con encode
    print('Resultado:',texto.encode('utf-8'))
    archivo.write(texto.encode('utf-8'))

print('-----------------------------------------------')
with open("Mitextobinario.bin", "rb") as archivo:
    texto = archivo.read()
    print(texto)
    print(texto.decode("utf-8"))
    print('-----------------------------------------------')
    archivo.seek(0)
    texto=archivo.read(3)
    print ('primeros 3: ',texto)
    texto = archivo.read(3)
    print('otros 3: ',texto)
    archivo.seek(10,1)  #DE la current 10 para adelante
    texto = archivo.read(3)
    print('de la ultima me muevo 10 hacia delante',texto)
    print('-----------------------------------------------')
    archivo.seek(0)
    texto=archivo.read(3)
    print (texto)
    archivo.seek(-5,2) ## De la ultima -5
    texto = archivo.read(3)
    print(texto)
