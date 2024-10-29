# -*- coding: utf-8 -*-
class color:
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"

    def mensaje(texto):
        print(f"\n{color.BLUE}[{color.ENDC}{color.GREEN}+{color.ENDC}{color.BLUE}] {texto}{color.ENDC}")
    def mensaje_exito(texto):
        print(f"\n{color.BLUE}[{color.ENDC}{color.GREEN}+{color.ENDC}{color.BLUE}]{color.ENDC} {color.GREEN}{texto}{color.ENDC}")
    def mensaje_error(texto, signo="-"):
        print(f"\n{color.YELLOW}[{color.ENDC}{color.RED}{signo}{color.ENDC}{color.YELLOW}]{color.ENDC}{color.RED} {texto}{color.ENDC}")
    def mensaje_input(texto, tipo=int):
        try:
            opcion = tipo(input(f"{color.YELLOW}[{color.ENDC}{color.RED}!{color.ENDC}{color.YELLOW}] {texto}: {color.ENDC}"))
            return opcion
        except ValueError:
            return False

class Turno:
    def __init__(self, numero_turno, paciente_nombre, horario_turno, estado, edad, fecha_turno):
        self.numero_turno = numero_turno
        self.paciente_nombre = paciente_nombre
        self.horario_turno = horario_turno
        self.edad = edad
        self.estado = estado
        self.fecha_turno = fecha_turno

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
    def setEstado(self, estado):
        self.estado = estado

    def __str__(self):
        return f"{self.numero_turno},{self.paciente_nombre},{self.horario_turno},{self.estado},{self.edad},{self.fecha_turno}"

def menu():
    print(f"\n[*] {color.BLUE}1. Importar Turnos desde archivo{color.ENDC}")
    print(f"[*] {color.BLUE}2. Atender Siguiente Turno{color.ENDC}")
    print(f"[*] {color.BLUE}3. Cancelar Turno{color.ENDC}")
    print(f"[*] {color.BLUE}4. Buscar Turno por Numero{color.ENDC}")
    print(f"[*] {color.BLUE}5. Ordenar Turnos por Horario{color.ENDC}")
    print(f"[*] {color.BLUE}6. Insertar Sobreturno{color.ENDC}")
    print(f"[*] {color.BLUE}7. Mostrar Turnos Pendientes / Tomados / Cancelados{color.ENDC}")
    print(f"[*] {color.BLUE}8. Mostrar Log de turnos historicos{color.ENDC}")
    print(f"[*] {color.RED}9. Salir{color.ENDC}\n")
    opcion = color.mensaje_input("Por favor, seleccione una opción")
    return opcion

#1
def importar_turnos(lista_turnos, ruta):
    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()
        if len(lineas) == 10:
            for linea in lineas:
                dato_turno = linea.strip().split(',')
                turno = Turno(dato_turno[0], #El primer dato es el número de turno
                            dato_turno[1], #El segundo dato es el nombre del paciente
                            dato_turno[2], #El tercer dato es el horario del turno
                            dato_turno[3], #El cuarto dato es el estado del turno
                            dato_turno[4], #El quinto dato es la edad del paciente
                            dato_turno[5]) #El sexto dato es la fecha del turno
                lista_turnos.append(turno)
            color.mensaje_exito("Turnos importados con éxito.")
            mostrar_turnos(lista_turnos)
        else:
            color.mensaje_error("La cantidad de turnos deben ser exactamente 10.")

#1.2
def mostrar_turnos(lista_turnos, c=color.YELLOW):
    print(f"\n{color.UNDERLINE}{color.BLUE}{'Número':<10} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}{color.ENDC}{color.ENDC}")
    for turno in lista_turnos:
        print(f"{turno.getNumeroTurno():<10} {turno.getPacienteNombre():<20} {turno.getHorarioTurno():<10} {c}{turno.getEstado():<10}{color.ENDC} {turno.getEdad():<5} {turno.getFechaTurno():<15}")

# Muestra 1 solo turno
def mostrar_turno(lista_turnos, index=0, c=color.YELLOW):
    turno = lista_turnos[index]
    print(f"\n{color.UNDERLINE}{color.BLUE}{'Número':<10} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}{color.ENDC}{color.ENDC}")
    print(f"{turno.getNumeroTurno():<10} {turno.getPacienteNombre():<20} {turno.getHorarioTurno():<10} {c}{turno.getEstado():<10}{color.ENDC} {turno.getEdad():<5} {turno.getFechaTurno():<15}")

#2
def atender_turnos(lista_turnos, lista_turnos_historicos, ruta_historicos):
    with open(ruta_historicos, "a") as archivo:
        turno = lista_turnos[0]
        turno.setEstado("tomado")
        lista_turnos_historicos.append(turno)
        archivo.write(str(turno) + "\n")
        lista_turnos.remove(turno)
        color.mensaje_exito(f"Turno {turno.getNumeroTurno()} atendido.")
        mostrar_turno(lista_turnos_historicos, int(len(lista_turnos_historicos)-1), color.GREEN)

#3
def cancelar_turnos(lista_turnos, lista_turnos_historicos, ruta_historicos):
    with open(ruta_historicos, "a") as archivo:
        turno = lista_turnos[0]
        turno.setEstado("cancelado")
        lista_turnos_historicos.append(turno)
        archivo.write(str(turno) + "\n")
        lista_turnos.remove(turno)
        color.mensaje_exito(f"Turno {turno.getNumeroTurno()} cancelado.")
        mostrar_turno(lista_turnos_historicos, int(len(lista_turnos_historicos)-1), color.RED)

#4 BUSQUEDA BINARIA
def buscar_turnos(lista_turnos, num_turno):
    inicio = 0
    fin = len(lista_turnos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        turno_actual = lista_turnos[medio]
        if int(turno_actual.getNumeroTurno()) == num_turno:
            return turno_actual
        elif int(turno_actual.getNumeroTurno()) < num_turno:
            inicio = medio + 1
        else:
            fin = medio - 1

#4.1 FUNCION HECHA PARA NO REPETIR CÓDIGO EN LA OPCIÓN 4
def mostrar_turno_buscados(turno, num_turno, c):
    color.mensaje_exito(f"Turno {num_turno} encontrado:")
    print(f"\n{color.UNDERLINE}{color.BLUE}{'Número':<10} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}{color.ENDC}{color.ENDC}")
    print(f"{turno.getNumeroTurno():<10} {turno.getPacienteNombre():<20} {turno.getHorarioTurno():<10} {c}{turno.getEstado():<10}{color.ENDC} {turno.getEdad():<5} {turno.getFechaTurno():<15}")

#5 ORDENAMIENTO POR BURBUJEO
def ordenar_turnos(lista_turnos):
    n = len(lista_turnos)
    cambio = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_turnos[j].getHorarioTurno() > lista_turnos[j + 1].getHorarioTurno():
                lista_turnos[j], lista_turnos[j + 1] = lista_turnos[j + 1], lista_turnos[j]
                cambio = True
    if not cambio:
        color.mensaje("Los turnos ya están ordenados:")
        mostrar_turnos(lista_turnos)
    else:
        color.mensaje_exito("Turnos ordenados:")
        mostrar_turnos(lista_turnos)

#6
def insertar_sobreturnos(lista_turnos):
    cant_turnos = len(lista_turnos)
    if cant_turnos < 10:
        try:
            num_turno = int(lista_turnos[-1].getNumeroTurno()) + 1
        except:
            num_turno = 1
        nombre = color.mensaje_input("Ingrese el nombre del paciente", str)
        while True:
            edad = color.mensaje_input("Ingrese la edad del paciente")
            if not 0 < edad < 100:
                color.mensaje_error("La edad debe ser representada en números. Intentelo de nuevo.\n")
                continue
            break
        while True:
            fecha_turno = color.mensaje_input("Ingrese la fecha del turno (YYYY-MM-DD)", str)
            if len(fecha_turno) != 10:
                color.mensaje_error("La fecha debe ser representada en formato (YYYY-MM-DD). Por ejemplo \"2024-06-06\". Intentelo de nuevo.\n")
                continue
            break
        while True:
            hora = color.mensaje_input("Ingrese el horario del turno (HH:MM)", str)
            if len(hora) != 5:
                color.mensaje_error("El horario debe ser representado en formato (HH:MM). Por ejemplo \"12:30\". Intentelo de nuevo.\n")
                continue
            break
        turno = Turno(num_turno, nombre, hora, "pendiente", edad, fecha_turno)
        lista_turnos.append(turno)
        color.mensaje_exito("Sobreturno insertado con éxito:")
        mostrar_turno(lista_turnos, int(len(lista_turnos)-1))
    else:
        color.mensaje_error("No se pueden agregar más turnos. Cupo máximo (10).")

#7 Mostrar Turnos Pendientes / Tomados / Cancelados
def mostrar_turnos_ptc(lista_turnos, lista_turnos_historicos):
    turnos_tomados = []
    turnos_cancelados = []
    for turno in lista_turnos_historicos:
        if turno.getEstado() == "tomado":
            turnos_tomados.append(turno)
        else:
            turnos_cancelados.append(turno)
    if len(lista_turnos) > 0:
        color.mensaje("Turnos pendientes del día:")
        mostrar_turnos(lista_turnos)
    if len(turnos_tomados) > 0:
        color.mensaje("Turnos tomados del día:")
        mostrar_turnos(turnos_tomados, color.GREEN)
    if len(turnos_cancelados) > 0:
        color.mensaje("Turnos cancelados del día:")
        mostrar_turnos(turnos_cancelados, color.RED)

#8
def mostrar_turnos_historicos(ruta_historico):
    turnos = []
    with open(ruta_historico, "r") as archivo:
        for linea in archivo:
            turnos.append(linea.strip().split(','))
        print(f"\n{color.UNDERLINE}{color.BLUE}{'Número':<10} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}{color.ENDC}{color.ENDC}")
        for turno in turnos:
            if turno[3] == "tomado":
                print(f"{turno[0]:<10} {turno[1]:<20} {turno[2]:<10} {color.GREEN}{turno[3]:<10}{color.ENDC} {turno[4]:<5} {turno[5]:<15}")
            else:
                print(f"{turno[0]:<10} {turno[1]:<20} {turno[2]:<10} {color.RED}{turno[3]:<10}{color.ENDC} {turno[4]:<5} {turno[5]:<15}")

def main():
    ruta = "C:/pyfiles/turnosdeldia.txt"
    ruta_historicos = "C:/pyfiles/turnoshistoricos.txt"
    #ruta = "turnosdeldia.txt"
    #ruta_historicos = "turnoshistoricos.txt"
    lista_turnos = []
    lista_turnos_historicos = []
    turnos_importados = False
    print("\n","="*10,f"{color.GREEN}Bienvenido al Sistema de Gestión de Turnos de Pacientes!{color.ENDC}","="*10)
    while True:
        opcion = menu()
        if opcion == 1 and turnos_importados == False:
            color.mensaje("Imoportando turnos...")
            try:
                importar_turnos(lista_turnos, ruta)
                turnos_importados = True
            except FileNotFoundError:
                color.mensaje_error("Error. No se pudo encontrar el archivo.")
        elif opcion == 2:
            color.mensaje("Atendiendo turno:")
            try:
                mostrar_turno(lista_turnos)
                atender_turnos(lista_turnos, lista_turnos_historicos, ruta_historicos)
            except:
                color.mensaje_error("No hay turnos para atender.")
        elif opcion == 3:
            color.mensaje("Cancelando turno:")
            try:
                mostrar_turno(lista_turnos)
                cancelar_turnos(lista_turnos, lista_turnos_historicos, ruta_historicos)
            except:
                color.mensaje_error("No hay turnos para cancelar.")
        elif opcion == 4 and turnos_importados == True:
            num_turno = color.mensaje_input("Por favor, introduzca un número de turno a buscar")
            turno = buscar_turnos(lista_turnos, num_turno)
            turno_historico = buscar_turnos(lista_turnos_historicos, num_turno)
            if turno:
                mostrar_turno_buscados(turno, num_turno, color.YELLOW)
            elif turno_historico and turno_historico.getEstado() == "tomado":
                mostrar_turno_buscados(turno_historico, num_turno, color.GREEN)
            elif turno_historico and turno_historico.getEstado() == "cancelado":
                mostrar_turno_buscados(turno_historico, num_turno, color.RED)
            else:
                color.mensaje_error(f"No se encontró un turno con el número: {num_turno}")
        elif opcion == 5 and turnos_importados == True:
            color.mensaje("Ordenando turnos...")
            ordenar_turnos(lista_turnos)
        elif opcion == 6 and turnos_importados == True:
            insertar_sobreturnos(lista_turnos)
        elif opcion == 7 and turnos_importados == True:
            mostrar_turnos_ptc(lista_turnos, lista_turnos_historicos)
        elif opcion == 8:
            try:
                color.mensaje("Log histórico de turnos:")
                mostrar_turnos_historicos(ruta_historicos)
            except FileNotFoundError:
                color.mensaje_error("Error. No se pudo encontrar el archivo.")
        elif opcion == 9:
            color.mensaje_error("Saliendo...", "+")
            break
        else:
            color.mensaje_error("Opción inválida. Por favor, seleccione una opción válida.")

main()