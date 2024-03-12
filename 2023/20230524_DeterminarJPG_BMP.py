# -*- coding: utf-8 -*-
def udf_verificar_formato_binario(archivo):
    try:
        with open(archivo, 'rb') as f:
            # Leer los primeros bytes del archivo
            bytes_iniciales = f.read(2)

            # Verificar el formato basado en los bytes iniciales
            if bytes_iniciales == b'\xff\xd8':
                print("El archivo es un JPG.")
            elif bytes_iniciales == b'\x42\x4d':
                print("El archivo es un BMP.")
            else:
                print("El archivo no es un JPG ni un BMP.")
    except IOError:
        print("No se pudo abrir el archivo.")

# Llamar a la función y proporcionar la ruta de archivo
ruta_entrada = r'C:\Users\castili4\Pictures\foto_color.jpg'
udf_verificar_formato_binario(ruta_entrada)