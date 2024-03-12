# -*- coding: utf-8 -*-

'''
from PIL import Image

def convertir_a_bn(archivo_entrada, archivo_salida):
    try:
        imagen = Image.open(archivo_entrada)
        imagen_bn = imagen.convert("L")  # Convertir a escala de grises (blanco y negro)
        imagen_bn.save(archivo_salida)

        print("La conversión a blanco y negro se ha completado con éxito.")
    except IOError:
        print("No se pudo abrir o escribir en los archivos.")

# Llamar a la función y proporcionar las rutas de archivo de entrada y salida
convertir_a_bn("imagen_color.jpg", "imagen_bn.jpg")
'''

def convert_to_bw(input_file, output_file):
    try:
        with open(input_file, 'rb') as f_in:
            # Read the binary content of the input file
            content = f_in.read()

            # Find the position where the pixel data starts
            start_position = content.find(b'\xFF\xC0')

            if start_position == -1:
                print("The file is not a valid JPG.")
                return

            # Modify the pixel data to black and white
            pixel_data = bytearray(content[start_position:])
            for i in range(0, len(pixel_data), 3):
                # Calculate the average of RGB channels
                average = sum(pixel_data[i:i+3]) // 3
                # Set the RGB channels to the average value
                pixel_data[i:i+3] = [average] * 3

        with open(output_file, 'wb') as f_out:
            # Write the modified pixel data to the output file
            f_out.write(content[:start_position])
            f_out.write(pixel_data)

        print("Conversion to black and white completed successfully.")
    except IOError:
        print("Unable to open or write to the files.")







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
        return -1

def bmp_convertir_a_bn(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'rb') as f_in:
            # Leer el contenido del archivo de entrada
            contenido = f_in.read()

            # Verificar la firma de BMP
            if contenido[:2] != b'BM':
                print("El archivo no es un BMP válido.")
                return

            # Obtener el offset donde comienza el arreglo de píxeles
            offset = int.from_bytes(contenido[10:14], 'little')

            # Obtener el ancho y alto de la imagen
            ancho = int.from_bytes(contenido[18:22], 'little')
            alto = int.from_bytes(contenido[22:26], 'little')

            # Verificar el número de bits por píxel
            bits_por_pixel = int.from_bytes(contenido[28:30], 'little')
            if bits_por_pixel != 24:
                print("El archivo no es un BMP de 24 bits.")
                return

            # Realizar la conversión a blanco y negro
            nuevo_contenido = bytearray(contenido)
            for i in range(offset, len(nuevo_contenido), 3):
                # Calcular el promedio de los canales RGB
                promedio = sum(nuevo_contenido[i:i+3]) // 3
                # Establecer los canales RGB al valor promedio
                nuevo_contenido[i:i+3] = [promedio] * 3

        with open(archivo_salida, 'wb') as f_out:
            # Escribir el nuevo contenido en el archivo de salida
            f_out.write(nuevo_contenido)

        print("La conversión a blanco y negro se ha completado con éxito.")
    except IOError:
        print("No se pudo abrir o escribir en los archivos.")


# Ejemplo de uso
ruta_entrada = r'C:\Users\castili4\Pictures\imagen.jpeg'
ruta_salida = r'C:\Users\castili4\Pictures\BN.jpg'

if udf_verificar_formato_binario(ruta_entrada) == -1:
    print("El archivo no es un JPG válido.")
else:
    # Call the function and provide the input and output file paths
    convert_to_bw(ruta_entrada, ruta_salida)
    bmp_convertir_a_bn(ruta_entrada, ruta_salida)

