#encoding:UTF-8
import numpy as np


def udf_menu():
    """Función para mostrar el menú, obtener y validar la opción seleccionada."""
    while True:
        print("\nMenú Principal:")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Opción 5")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4', '5', '6']:
            return opcion
        else:
            print("Opción inválida. Intente nuevamente.")


def mi_main():
    mat_producto_cantidad = np.zeros((4, 3), dtype=int)
    mat_productos_valorizados = None
    """Función principal que ejecuta el programa."""
    while True:
        opcion = udf_menu()

        if opcion == '1':
            print("Seleccionó la opción 1")
        elif opcion == '2':
            print("Seleccionó la opción 2")
        elif opcion == '3':
            print("Seleccionó la opción 3")
        elif opcion == '4':
            print("Seleccionó la opción 4")
        elif opcion == '5':
            print("Seleccionó la opción 5")
        elif opcion == '6':
            print("Saliendo del programa...")
            break

#AreaGlobal
mi_main()
