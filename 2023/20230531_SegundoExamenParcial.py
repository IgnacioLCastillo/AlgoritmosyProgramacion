# -*- coding: utf-8 -*-
# Definición de la clase Examen
class TDAExamen:
    def __init__(self, idExamen, nombreEstudiante, notaEstudiante, materia):
        self.idExamen = idExamen
        self.nombreEstudiante = nombreEstudiante
        self.notaEstudiante = notaEstudiante
        self.materia = materia

    def ObteneridExamen(self):
        return self.idExamen

    def __str__(self):
        return f"{self.idExamen},{self.nombreEstudiante},{self.notaEstudiante},{self.materia}"


# Función para leer el archivo de texto y cargar los datos en una lista de Examen
def leer_archivo(nombre_archivo):
    lisexamenes=[]
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            print(lineas)
            for linea in lineas:
                datos = linea.strip().split(';')
                print (datos)
                examen = TDAExamen(datos[0], datos[1], float(datos[2]), datos[3])
                print(examen)
                lisexamenes.append(examen)
        print("Archivo leído correctamente.")
    except FileNotFoundError:
        print("El archivo no se encuentra en la ruta especificada.")
    except Exception as Otromensaje:
        print("Ocurrio un error al abrir el archivo:", Otromensaje)

    return lisexamenes

# Función para escribir la lista de Examen en el archivo de texto
def udf_escribir_archivo(plExamenes, nombre_archivo):
    with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
        for cadaExamen in plExamenes:
            linea = ';'.join(cadaExamen)
            archivo.write(str(cadaExamen) + '\n')


# Función para buscar un examen por ID en la lista de Examen
def udfBusquedaSecuencial(unaLista, item):
    pos = 0
    while pos < len(unaLista):
        if unaLista[pos].ObteneridExamen() == item:
            return pos
        else:
            pos = pos+1
    return -1


def buscar_examen(examenes, id_examen):
    for examen in examenes:
        if examen.idExamen == id_examen:
            return examen
    return None

def udf_modificar_examen(plistaestudiantes, pindice, pnueva_nota):
    unestudiante = plistaestudiantes[pindice]
    unestudiante.notaEstudiante = pnueva_nota



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
    ruta = r"c:\pyfiles\examenes.txt"
    nombre_archivo = ruta
    while True:
        print("1) Leer archivo de texto")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Buscar")
        print("5) Opcion 5")
        print("6) Opcion 6")
        print("7) Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            listaexamenes = leer_archivo(nombre_archivo)
            udfMostrarTodos(listaexamenes)

        if opcion == 2:
            print("--------------Modifica Examen--------------")
            idBuscado = input("Ingrese el ID a Modificar:")
            encontrado = udfBusquedaSecuencial(listaexamenes, idBuscado)
            if encontrado == -1:
                print(f"Examen ID{idBuscado} no encontrado en la lista")
            else:
                print(f"El Examen{listaexamenes[encontrado]} , se Modificara")

                nuevaNota=float(input("Ingrese la nueva Nota:"))

                udf_modificar_examen(listaexamenes, encontrado, nuevaNota)

                udf_escribir_archivo(listaexamenes,nombre_archivo)
                udfMostrarTodos(listaexamenes)
                print("Examen Modificado con Exito")


        if opcion == 3:
            print("--------------Elimina Examen--------------")
            idBuscado = input("Ingrese el ID a Eliminar:")
            encontrado = udfBusquedaSecuencial(listaexamenes, idBuscado)
            if encontrado == -1:
                print(f"Examen ID{idBuscado} no encontrado en la lista")
            else:
                print(f"El Examen{listaexamenes[encontrado]} , se eliminara")
                listaexamenes.remove(listaexamenes[encontrado])
                udf_escribir_archivo(listaexamenes,nombre_archivo)
                udfMostrarTodos(listaexamenes)
                print("Examen Eliminado con Exito")


        elif opcion == 7:
            print ("Salir")
            break

main()