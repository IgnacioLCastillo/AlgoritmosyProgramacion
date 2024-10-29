# -*- coding: utf-8 -*-

# Definimos el TDA para la información de cada vuelta
class TDA_Vuelta:
    def __init__(self, pnumero_vuelta, pvelocidad_vuelta, plitros_combustible_consumido):
        self.numero_vuelta = pnumero_vuelta
        self.velocidad_vuelta = pvelocidad_vuelta
        self.litros_combustible_consumido = plitros_combustible_consumido

# Función para mostrar el menú
def udf_mi_menu():
    print("\n--- Menú ---")
    print("1) Registro de Vuelta")
    print("2) Informe de performance")
    print("3) Salir")
    opcion = input("Elige una opción: ")
    return opcion


# Función principal (main)
def udf_mi_main():
    lis_vueltas = []
    while True:
        opcion = udf_mi_menu()
        if opcion == "1":
            print("Opción 1 seleccionada: Registro de Vuelta.")
        elif opcion == "2":
            print("Opción 2 seleccionada: Informe de performance.")
        elif opcion == "3":
            print("Opción 3 seleccionada: Salir del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

# Ejecutar el programa
udf_mi_main()
