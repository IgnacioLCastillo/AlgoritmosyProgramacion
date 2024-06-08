# -*- coding: utf-8 -*-
class Turno:
    def __init__(self, pnumero_turno, ppaciente_nombre, phorario_turno, pestado, pedad, pfecha_turno):
        self.numero_turno = pnumero_turno
        self.paciente_nombre = ppaciente_nombre
        self.horario_turno = phorario_turno
        self.edad = pedad
        self.estado = pestado
        self.fecha_turno = pfecha_turno

    def getNumeroTurno(self):
        return self.numero_turno
    def getPacienteNombre(self):
        return self.paciente_nombre
    def getHorarioTurno(self):
        return self.horario_turno
    def getEstado(self):
        return self.estado
    def getEdad(self):
        return self.edad
    def getFechaTurno(self):
        return self.fecha_turno

    def __str__(self):  # Método para convertir el objeto a string
        return f"{self.numero_turno},{self.paciente_nombre},{self.horario_turno},{self.estado},{self.pedad},{self.fecha_turno}"

def mostrar_menu():
    print("Bienvenido al Sistema de Gestión de Turnos de Pacientes\n")
    print("1. Importar Turnos desde archivo")
    print("2. Atender Siguiente Turno")
    print("3. Cancelar Turno")
    print("4. Buscar Turno por Número")
    print("5. Ordenar Turnos por Horario")
    print("6. Insertar Sobreturno")
    print("7. Mostrar Turnos Pendientes / Tomados / Cancelados")
    print("8. Mostrar Log de turnos historicos")
    print("9. Salir")
    # Otras opciones del menú
    opcion = input("Por favor, seleccione una opción: ")
    return opcion

def udf_importar_turnos_encola_inicial(plistaturnos,pruta):
    archivo = open(pruta, "r")
    for linea in archivo:
        linea = linea.rstrip("\n")
        cadadatodelturno = linea.split(",")
        turno = Turno(cadadatodelturno[0], #El primer dato es el número de turno
                      cadadatodelturno[1], #El segundo dato es el nombre del paciente
                      cadadatodelturno[2], #El tercer dato es el horario del turno
                      cadadatodelturno[3], #El cuarto dato es el estado del turno
                      cadadatodelturno[4], #El quinto dato es la edad del paciente
                      cadadatodelturno[5]) #El sexto dato es la fecha del turno
        plistaturnos.append(turno)

    archivo.close()

def udf_mostrar_turnos_importados(plistaturnos):
    # Imprimir encabezado de la tabla
    print(f"{'Número':<15} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}")
    # Iterar sobre cada turno en la lista de turnos
    for cadaTurno in plistaturnos:
        # Imprimir cada turno con formato tabular
        print(f"{cadaTurno.getNumeroTurno():<15} {cadaTurno.getPacienteNombre():<20} {cadaTurno.getHorarioTurno():<10} {cadaTurno.getEstado():<10} {cadaTurno.getEdad():<5} {cadaTurno.getFechaTurno():<15}")


# Programa principal
def miMain():
    ruta = r"C:\pyfiles\turnosdeldia.txt"
    ruta_historicos = r"C:\pyfiles\turnoshistoricos.txt"
    lista_turnos = []
    turnosHistoricos=[]
    while True:
        mipcion=mostrar_menu()
        if mipcion == '1':
            print("Importar Turnos desde archivo")
            udf_importar_turnos_encola_inicial(lista_turnos,ruta)
            udf_mostrar_turnos_importados(lista_turnos)
        elif mipcion == '2':
            print("Atender Siguiente Turno (desencola)")
            print("Atencion Paciente:",lista_turnos[0].getPacienteNombre())
            lista_turnos[0].estado = "Atendido"
            turnosHistoricos.append(lista_turnos[0])

            lista_turnos.pop(0)
            udf_mostrar_turnos_importados(lista_turnos)
        elif mipcion == '3':
            print("Cancelar Turno (desencola)")
        elif mipcion == '7':
            print("Mostrar Turnos Pendientes / Tomados / Cancelados")
            udf_mostrar_turnos_importados(turnosHistoricos)

        # Realizar todas las demas opciones del menu
        elif mipcion == '9':
            print("Fin del Algoritmo")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


#*-*-*--**-*-* Area Publica
miMain()