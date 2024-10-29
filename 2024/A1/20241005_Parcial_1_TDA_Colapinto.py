# -*- coding: utf-8 -*-
# Definimos el TDA para la información de cada vuelta
class TDA_Vuelta:
    def __init__(self, numero_vuelta, tiempo_vuelta, litros_combustible):
        self.numero_vuelta = numero_vuelta
        self.tiempo_vuelta = tiempo_vuelta
        self.litros_combustible = litros_combustible

# Función para mostrar el menú
def udf_mi_menu():
    print("\n--- Menú ---")
    print("1) Registro de tiempos")
    print("2) Informe de performance")
    print("3) Salir")
    opcion = input("Elige una opción: ")
    return opcion

# Función para registrar los tiempos y litros
def udf_registrar_tiempos(plis_vueltas):

    combustible_inicial = 0

    # Validar que el combustible inicial sea mayor o igual a 250 litros
    while True:
        try:
            combustible_inicial = float(input("Ingresa la cantidad de litros de combustible que cargarás (mínimo 250 litros): "))
            if combustible_inicial >= 250:
                break
            else:
                print("Error: Debes ingresar al menos 250 litros. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

    combustible_restante = combustible_inicial
    for i in range(1, 6):
        # Validar el tiempo de la vuelta
        while True:
            try:
                tiempo_vuelta = float(input(f"Ingresa el tiempo de la vuelta {i} (en segundos): "))
                break
            except ValueError:
                print("Error: Debes ingresar un número válido.")

        plis_vueltas.append(TDA_Vuelta(i, tiempo_vuelta, combustible_restante))
        print(plis_vueltas[0].numero_vuelta)
        combustible_restante -= 50



# Función para mostrar el informe de performance
def udf_mostrar_performance(plis_vueltas):
    if not plis_vueltas:
        print("Error: Debes registrar los tiempos de las 5 vueltas antes de acceder al informe de performance.")
        return

    print("\n--- Resumen de las vueltas ---")
    for vuelta in plis_vueltas:
        print(f"Vuelta {vuelta.numero_vuelta} - Tiempo: {vuelta.tiempo_vuelta} segundos - Combustible restante: {vuelta.litros_combustible} litros.")


def udf_mostrar_promedio_vuelta(plis_vueltas):
    # Calcular el promedio de tiempos
    tiempo_acumulado = 0
    for vuelta in plis_vueltas:
        tiempo_acumulado += vuelta.tiempo_vuelta
    return tiempo_acumulado / len(plis_vueltas)

def udf_mostrar_mejor_vuelta(plis_vueltas):
    for objvuelta in plis_vueltas:
        if objvuelta.numero_vuelta==1:
            obj_mejorvuelta=objvuelta
        else:
            if objvuelta.tiempo_vuelta<obj_mejorvuelta.tiempo_vuelta:
                obj_mejorvuelta=objvuelta
    return obj_mejorvuelta


# Función principal (main)
def udf_mi_main():
    lis_vueltas = []
    while True:
        opcion = udf_mi_menu()
        if opcion == "1":
            udf_registrar_tiempos(lis_vueltas)
        elif opcion == "2":
            udf_mostrar_performance(lis_vueltas)
            vi_tiempo_promedio=udf_mostrar_promedio_vuelta(lis_vueltas)
            print(f"El tiempo promedio de las vueltas es: {vi_tiempo_promedio:.2f} segundos")
            mejor=udf_mostrar_mejor_vuelta(lis_vueltas)
            print(f"La mejor vuelta fue la número {mejor.numero_vuelta} con un tiempo de {mejor.tiempo_vuelta} segundos")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Ejecutar el programa
udf_mi_main()
