#encoding:UTF-8
import numpy as np


def udf_cargar_cantidades(p_mat_producto_cantidad):
    for i in range(4):
        for j in range(3):
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad para la categoría {i + 1}, trimestre {j + 1}: "))
                    if cantidad >= 0:
                        p_mat_producto_cantidad[i, j] = cantidad
                        break
                    else:
                        print("La cantidad debe ser mayor o igual a 0. Intente nuevamente.")
                except ValueError:
                    print("Entrada no válida. Intente nuevamente.")


def udf_proceso_valorizacion(p_mat_producto_cantidad):
    valores = [150, 50, 100]  # Almacen, Bebidas, Limpieza
    mat_productos_valorizados = np.zeros_like(p_mat_producto_cantidad, dtype=float)
    for i in range(3):
        for j in range(3):
            mat_productos_valorizados[i, j] = p_mat_producto_cantidad[i, j] * valores[i]
    return mat_productos_valorizados


def udf_maximo_categoria(p_mat_productos_valorizados, p_categoria):
    max_valor = -1
    max_trimestre = -1
    for trimestre in range(3):
        if p_mat_productos_valorizados[p_categoria, trimestre] > max_valor:
            max_valor = p_mat_productos_valorizados[p_categoria, trimestre]
            max_trimestre = trimestre
    return max_valor, max_trimestre + 1


def udf_guardar_datos(p_mat_producto_cantidad, p_mat_productos_valorizados, archivo_cantidades="cantidades.txt",
                      archivo_valorizacion="valorizacion.txt"):
    with open(archivo_cantidades, 'w') as file:
        for fila in p_mat_producto_cantidad:
            for elemento in fila:
                file.write(f"{elemento} ")
            file.write("\n")

    with open(archivo_valorizacion, 'w') as file:
        for fila in p_mat_productos_valorizados:
            for elemento in fila:
                file.write(f"{elemento} ")
            file.write("\n")


def udf_consultar_precios(p_mat_productos_valorizados):
    while True:
        categoria = int(input("Ingrese el número de la categoría (1: Almacen, 2: Bebidas, 3: Limpieza): ")) - 1
        if 0 <= categoria < 3:
            print(f"Precios valorizados para la categoría {categoria + 1}: {p_mat_productos_valorizados[categoria]}")
            break
        else:
            print("Categoría inválida. Intente nuevamente.")


def udf_menu():
    while True:
        print("\nMenú Principal:")
        print("1. Carga de Cantidades")
        print("2. Proceso de Valorización")
        print("3. Consultar Categoría y Trimestre más Vendido")
        print("4. Consultar Precios por Categoría")
        print("5. Guardar Datos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4', '5', '6']:
            return opcion
        else:
            print("Opción inválida. Intente nuevamente.")


def mi_main():
    mat_producto_cantidad = np.zeros((4, 3), dtype=int)
    mat_productos_valorizados = None
    carga_realizada = False

    while True:
        opcion = udf_menu()

        if opcion == '1':
            if not carga_realizada:
                udf_cargar_cantidades(mat_producto_cantidad)
                carga_realizada = True
            else:
                print("Las cantidades ya han sido cargadas.")
        elif opcion == '2':
            if carga_realizada:
                mat_productos_valorizados = udf_proceso_valorizacion(mat_producto_cantidad)
                print("Proceso de valorización completado.")
            else:
                print("Debe cargar las cantidades primero.")
        elif opcion == '3':
            if mat_productos_valorizados is not None:
                categoria = int(input("Ingrese el número de la categoría (1: Almacen, 2: Bebidas, 3: Limpieza): ")) - 1
                if 0 <= categoria < 3:
                    max_valor, max_trimestre = udf_maximo_categoria(mat_productos_valorizados, categoria)
                    print(f"Categoría: {categoria + 1}, Máximo valor: {max_valor}, Trimestre: {max_trimestre}")
                else:
                    print("Categoría inválida. Intente nuevamente.")
            else:
                print("Debe realizar el proceso de valorización primero.")
        elif opcion == '4':
            if mat_productos_valorizados is not None:
                udf_consultar_precios(mat_productos_valorizados)
            else:
                print("Debe realizar el proceso de valorización primero.")
        elif opcion == '5':
            if carga_realizada and mat_productos_valorizados is not None:
                udf_guardar_datos(mat_producto_cantidad, mat_productos_valorizados)
                print("Datos guardados correctamente.")
            else:
                print("Debe cargar las cantidades y realizar el proceso de valorización primero.")
        elif opcion == '6':
            print("Saliendo del programa...")
            break

####Area global
mi_main()
