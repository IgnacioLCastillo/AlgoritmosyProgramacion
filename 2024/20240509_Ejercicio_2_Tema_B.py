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

def udfNoRepetido(plisProductos, pCodigo,phasta):
    if plisProductos[0] != 0:
        for i in range(phasta):
            if plisProductos[i].codigo == pCodigo:
                return False
        return True
    else:
        return True

def udfCargar_datos(lisProductos, viTopeLista):
    for i in range(viTopeLista):
        while True:
            miCodigo = int(input("Ingrese el código del producto: "))
            if udfNoRepetido(lisProductos, miCodigo,i):
                break
            else:
                print("Error: El código del producto ya existe.")
                continue

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

        lisProductos[i] = tdaProducto(miCodigo, stock, precio)

def udfProductoMasStock(lisProductos):
    mayor_stock = 0
    for producto in lisProductos:
        if producto.stock >= mayor_stock:
            mayor_stock = producto.stock
            productoMaximo=producto

    return productoMaximo


def udfMiMain():
    viTopeLista = 5
    lisProductos = [0] * viTopeLista
    viOpcion = -1
    while viOpcion != 3:
        print('\nMenú:')
        print('1- Cargar datos del vector estructura')
        print('2- Producto Mas Stock')
        print('3- Salir')
        viOpcion = int(input("Seleccione una opción: "))
        if viOpcion == 1:
            udfCargar_datos(lisProductos, viTopeLista)
        elif viOpcion == 2:
            productoMaximo=udfProductoMasStock(lisProductos)
            print(f'El producto con mayor stock es: {productoMaximo.Codigo} con {productoMaximo.stock} unidades.')
        elif viOpcion == 3:
            print("Saliendo del programa...")
        else:
            print('Error: Opción no válida.')

# Programa Principal
udfMiMain()
