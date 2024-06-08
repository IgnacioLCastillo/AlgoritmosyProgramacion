# -*- coding: utf-8 -*-
class tdaProductos:
    def __init__(self, pCodigoProducto, pStock, pPrecio=0):
        self.codigo = pCodigoProducto
        self.stock = pStock
        self.precio = pPrecio

    def __str__(self):
        return str(self.codigo) + ' ' + str(self.stock) + ' ' + str(self.precio)


def udfCargaproducto(lisProductos):
    for i in range(5):
        while True:
            try:
                vfCodigo = int(input(f"Ingrese el codigo del producto {i + 1}: "))
                if vfCodigo < 0:
                    print("Error, ingrese un número válido.")
                    continue
                break
            except ValueError:
                print("El código debe ser un número válido.")
                continue

        while True:
            try:
                pStock = int(input(f"Ingrese la cantidad de producto {i + 1}: "))
                if pStock < 0:
                    print("El stock debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("El stock debe ser un número válido.")
                continue

        while True:
            try:
                pPrecio = float(input(f"Ingrese el precio del producto {i + 1}: "))
                if pPrecio < 0:
                    print("El precio debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("El precio debe ser un número válido.")
                continue

        lisProductos.append(tdaProductos(vfCodigo, pStock, pPrecio))
        print(f'Producto {i + 1} cargado con éxito')


def udfObtenerEmpMaximo(lisProductos):
    max_stock = max(lisProductos, key=lambda x: x.stock)
    return lisProductos.index(max_stock)


def udfMiMain():
    viTopeLista = 5
    lisProductos = []*viTopeLista
    viOpcion = -1
    while viOpcion != 3:
        print('\n')
        print('1 - Opción 1: Cargar productos')
        print('2 - Opción 2: Obtener producto con mayor stock')
        print('3 - Salir')
        viOpcion = int(input("Seleccione una opción: "))

        if viOpcion == 1:
            udfCargaproducto(lisProductos)
            print("-------------- Opción 1 --------------")
        elif viOpcion == 2:
            if lisProductos:
                max_index = udfObtenerEmpMaximo(lisProductos)
                print(f"Producto con mayor stock: {lisProductos[max_index]}")
            else:
                print("La lista de productos está vacía.")
            print("-------------- Opción 2 --------------")
        elif viOpcion == 3:
            print("Hasta luego.")
        else:
            print('Opción no válida.')
            break


# Programa Principal
udfMiMain()
