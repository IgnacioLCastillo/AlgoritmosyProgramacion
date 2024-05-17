# -*- coding: utf-8 -*-
class tdaProducto:
    def __init__(self, pCodigoProducto, pStock, pPrecio=0):
        self.codigo = pCodigoProducto
        self.stock = pStock
        self.precio = pPrecio

    def __str__(self):
        return str(self.codigo) + ' ' + str(self.stock) + ' ' + str(self.precio)


def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        print("Error: El stock debe ser mayor o igual a 0.")
        return False

def validar_precio(precio):
    if precio >= 0:
        return True
    else:
        print("Error: El precio debe ser mayor o igual a 0.")
        return False

def udfCargar_datos(lisProductos, viTopeLista):
    for i in range(viTopeLista):
        print(f"\nProducto {i+1}:")
        codigo = i
        stock = int(input("Ingrese el stock del producto: "))
        while not validar_stock(stock):
            stock = int(input("Ingrese el stock del producto: "))

        while True:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: El precio debe ser mayor o igual a 0.")
                continue
            else:
                break

        lisProductos[i] = tdaProducto(codigo, stock, precio)

def udfCalcular_precio_promedio(lisProductos, viTopeLista):
    total_precios = sum(producto.precio for producto in lisProductos)
    '''
    # Otra forma de calcular el precio promedio y retornarlo
    for i in range(viTopeLista):
        total_precios += lisProductos[i].precio
    
    if viTopeLista == 0:
        return 0
    else:
        return total_precios / viTopeLista'''

    return total_precios / viTopeLista if viTopeLista > 0 else 0

def udfInformar_productos_precio_promedio(lisProductos, viTopeLista):
    precio_promedio = udfCalcular_precio_promedio(lisProductos, viTopeLista)
    print("\nProductos por encima del precio promedio:")
    for producto in lisProductos:
        if producto.precio > precio_promedio:
            print(producto)

def udfInformar_productos_reponer(lisProductos, viTopeLista):
    print("\nProductos que deben reponerse (Stock menor a 10 unidades):")
    for producto in lisProductos:
        if producto.stock < 10:
            print(producto)

def udfMiMain():
    viTopeLista = 5
    lisProductos = [0] * viTopeLista
    viOpcion = -1
    while viOpcion != 4:
        print('\nMenú:')
        print('1- Cargar datos del vector estructura')
        print('2- Informar productos por encima del precio promedio')
        print('3- Informar productos que deben reponerse')
        print('4- Salir')
        viOpcion = int(input("Seleccione una opción: "))
        if viOpcion == 1:
            udfCargar_datos(lisProductos, viTopeLista)
        elif viOpcion == 2:
            udfInformar_productos_precio_promedio(lisProductos, viTopeLista)
        elif viOpcion == 3:
            udfInformar_productos_reponer(lisProductos, viTopeLista)
        elif viOpcion == 4:
            print("Saliendo del programa...")
        else:
            print('Error: Opción no válida.')

# Programa Principal
udfMiMain()
