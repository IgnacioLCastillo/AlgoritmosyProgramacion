# -*- coding: utf-8 -*-
# Definición de la clase Examen
class Examen:
    def __init__(self, idExamen, nombreEstudiante, notaEstudiante, materia):
        self.idExamen = idExamen
        self.nombreEstudiante = nombreEstudiante
        self.notaEstudiante = notaEstudiante
        self.materia = materia

    def __str__(self):
        return f"{self.idExamen},{self.nombreEstudiante},{self.notaEstudiante},{self.materia}"


# Función para leer el archivo de texto y cargar los datos en una lista de Examen
def leer_archivo(nombre_archivo):
    examenes=[]
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            print(lineas)
            for linea in lineas:
                datos = linea.strip().split(';')
                examen = Examen(datos[0], datos[1], float(datos[2]), datos[3])
                examenes.append(examen)
        print("Archivo leído correctamente.")
    except FileNotFoundError:
        print("El archivo no se encuentra en la ruta especificada.")
    except Exception as Otromensaje:
        print("Ocurrio un error al abrir el archivo:", Otromensaje)

    return examenes

# Función para escribir la lista de Examen en el archivo de texto
def escribir_archivo(plExamenes, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for cadaExamen in plExamenes:
            archivo.write(str(cadaExamen) + '\n')


# Función para buscar un examen por ID en la lista de Examen
def buscar_examen(examenes, id_examen):
    for examen in examenes:
        if examen.idExamen == id_examen:
            return examen
    return None


# Función para ordenar la lista de Examen por nota usando el método de burbuja
def ordenar_por_nota(examenes):
    n = len(examenes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if examenes[j].notaEstudiante > examenes[j + 1].notaEstudiante:
                examenes[j], examenes[j + 1] = examenes[j + 1], examenes[j]


# Función para realizar una búsqueda binaria de una nota en la lista de Examen
def buscar_nota(examenes, nota):
    izquierda = 0
    derecha = len(examenes) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if examenes[medio].notaEstudiante == nota:
            return examenes[medio]
        elif examenes[medio].notaEstudiante < nota:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None


def udfMostrarTodos(plisNota):
    for cadaExamen in plisNota:
        print(cadaExamen)


# Función principal del programa
def main():
    ruta = r"c:\pyfile\examenes.txt"
    nombre_archivo = ruta
    while True:
        print("1) Leer archivo de texto")
        print("2) Modificar atributo de un examen")
        print("3) Eliminar un examen")
        print("4) Informar examenes ordenados por nota")
        print("5) Buscar una nota mediante búsqueda binaria")
        print("6) Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            examenes = leer_archivo(nombre_archivo)

            udfMostrarTodos(examenes)
        elif opcion == 2:
            print ("Opcion 2")

main()