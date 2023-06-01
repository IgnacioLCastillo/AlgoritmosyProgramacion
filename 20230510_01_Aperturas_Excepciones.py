
print('-------------Metodo Apertura Capturando exceptions------------------')
try:
    print("Abierto con Exito")
    fdarchivo =  open("mi_assssrchivo.txt", "r")
    contenido = fdarchivo.read()
    print(contenido)
    fdarchivo.close()
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")
except Exception as Otromensaje:
    print("Ocurrio un error al abrir el archivo:", Otromensaje)
finally:
    print("paso a cerrar si o si")



with open("Mitexto.txt", "w") as archivo:
    lista_lineas = ["Hola, mundo!\n", "Este es un ejemplo de creacion y escritura en un archivo.\n", "Tres Lineas!\n"]
    archivo.writelines(lista_lineas)



print('-------------Con Read Mostrado todo el contenido. Luegi el Tell------------------')
try:
    with open('nombres.txt', 'r') as archivo:
        contenido = archivo.read()  # Levantamos_todo el contenido
        print('primer read:',contenido)
        print(archivo.tell())
        archivo.seek(0)
        print(archivo.tell())
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")
except Exception as Otromensaje:
    print("Ocurrio un error al abrir el archivo:", Otromensaje)
