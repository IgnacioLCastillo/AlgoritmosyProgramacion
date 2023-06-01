# -*- coding: utf-8 -*-
# Representando un carácter especial en una cadena de bytes
cadena_bytes = b'Campe\xc3\xb3n del mundo'  # \xe1 representa el carácter 'ó' en UTF-8
print(cadena_bytes)  # b'Hola \xe1 mundo'
print(cadena_bytes.decode("utf-8"))