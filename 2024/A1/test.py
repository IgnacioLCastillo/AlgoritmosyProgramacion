class Registros:
    def __init__(self,tiempo_vuelta, num_vuelta, combustible_lts):
        self.tiempo_vuelta= tiempo_vuelta
        self.num_vuelta= num_vuelta
        self.combustible_lts= combustible_lts

def cargar_tiempos(self,list_vueltas,tiempo_vuelta, combustible_restante):
    total_combustible = []
    for i in range(5):
        print(f" Ingresar el tiempo de cada una de las 5 vueltas, el primero {i +1} : ")
        tiempo_vuelta= input("ingrese el tiempo de la primera vuelta: ")
        combustible_restante=input("Cuando combustible resta despues de cada vuelta: ")
        if combustible_restante <= 250:
            print("debe ser mayor a 250 litros.")
        else:

            total_combustible.append(combustible_restante)
            print("dato ingresado")

            num_vuelta= input("ingrese el numero de vuelta: ")


            list_vueltas.append(num_vuelta, tiempo_vuelta, combustible_restante)



def mostrar_resumen(self, list_vueltas, tiempo_vuelta, combustible_restante):
        for tiempo in list_vueltas:
            print(f"Los tiempos cargados son:{tiempo_vuelta():2f} , el combustible final despues de cada vuelta: {combustible_restante}")

def mejor_vuelta(self,tiempo_vuelta, list_vueltas):
    vuelta_rapida= tiempo_vuelta[0]
    for mj_tiempo in list_vueltas:
         if tiempo_vuelta < vuelta_rapida:
            vuelta_rapida= mj_tiempo
    return vuelta_rapida

def calcular_tiempo_promedio(self, tiempo_vuelta,list_vueltas, num_vueltas):
    total_tiempo= sum(list_vueltas)

    return total_tiempo/ len(num_vueltas)

def combustible_sobrado(self,combustible_restante,total_combustible):
    combustible_final= total_combustible - combustible_restante
    return combustible_final
def udf_mi_menu():
    print("\n--- Menú ---")
    print("1) Registro de tiempos")
    print("2) Informe de performance")
    print("3) Salir")
    opcion = input("Elige una opción: ")
    return opcion



def udf_mi_main():
    list_vueltas = []
    while True:
        opcion = udf_mi_menu()
        if opcion == "1":
            print("Opción 1 seleccionada: Registro de tiempos.")
            cargar_tiempos()
        elif opcion == "2":
            print("Opción 2 seleccionada: Informe de performance.")
        elif opcion == "3":
            print("Opción 3 seleccionada: Salir del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

udf_mi_main()


