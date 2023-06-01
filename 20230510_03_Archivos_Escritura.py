# -*- coding: utf-8 -*-
with open("Mitexto.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Argentina es tricampeon mundial.\n")
    archivo.write("Que locura!\n")
    archivo.write("Campeones")

#flush(): Este método se utiliza para asegurarse de que todos los datos escritos en el archivo se hayan guardado
# físicamente en el disco. En general, Python realiza un almacenamiento en búfer de los datos escritos en el archivo
# para mejorar la eficiencia. Sin embargo, puede haber casos en los que desees forzar la escritura inmediata de los
# datos en el archivo.

with open("Mitexto.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.flush()
    archivo.write("Argentina es tricampeon mundial.\n")
    archivo.flush()
    archivo.write("Que locura!")
    archivo.flush()
    archivo.write("Campeones")



with open("Mitexto.txt", "w") as archivo:
    lista_lineas = ["Hola, mundo!\n", "Este es un ejemplo de escritura en un archivo.\n", "Tres Lineas!\n"]
    archivo.writelines(lista_lineas)


print('-------------Leo de UN Archivo y Grabo en otro------------------')
with open("nombres.txt", "r") as archivo:
        todaslineas = archivo.readlines()

with open("Mitexto.txt", "w") as archivo:
    lista_lineas = ["Hola, mundo!\n", "Este es un ejemplo de escritura en un archivo.\n", "Tres Lineas!\n"]
    archivo.writelines(lista_lineas)
    archivo.writelines(todaslineas)



print('-------------Lectura y Escritura. Si Uso W+ crea el archivo------------------')
with open("Mitexto.txt", "r+") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.writelines(["Agrego esto\n", "y esto\n"])
    archivo.seek(0)
    todaslineas = archivo.read()
    print(todaslineas)
'''
print('-------------Con Read Mostrado todo el contenido. Luegi el Tell------------------')
with open('Mitexto.txt', 'r') as archivo:
    contenido = archivo.read()  # Levantamos todo el contenido
    print(contenido)

print('-------------Hago Append en el otro archivo con lo que tienen MiTexto------------------')
with open('nombres.txt', 'a') as archivo:
    archivo.write(contenido)
'''
#ruta = r"C:\Users\castili4\PycharmProjects\pythonProject\Algoritmos y Programacion\Rawarchivo.txt"
#ruta = "C:/Users/castili4/PycharmProjects/pythonProject/Algoritmos y Programacion/Rawarchivo.txt"
#ruta = "C:\\Users\\castili4\\PycharmProjects\\pythonProject\\Algoritmos y Programacion\\Rawarchivo.txt"
ruta = r"C:\Users\castili4\PycharmProjects\pythonProject\Algoritmos y Programacion\Rawarchivo.txt"
with open(ruta, "w") as archivo:
    archivo.write("Viene desde el Raw!\n")

with open(ruta, "a") as archivo:
    archivo.write("al fondo que hay lugar!\n")


