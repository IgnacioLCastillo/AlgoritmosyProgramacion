class tdaProducto:
    def __init__(self, cod, stock, precio):
        self.codigo = cod
        self.cantStock = stock
        self.precioProducto = precio

    def obtenerStock(self):
        return self.cantStock

    def __str__(self):
        return self.codigo

def cargaListaProductos(lista, cantElem):
    contador = 0
    for i in range(0, cantElem, 1):
        codigo = (input("Ingrese codigo de producto: "))

        while True:
            try:
                cantidadStock = int(input("Ingrese stock del producto: "))
                if cantidadStock < 0:
                    print("Ingrese un numero positivo, por favor")
                    continue
            except ValueError:
                print("Ingrese un numero, por favor")
                continue
            else:
                break

        while True:
            try:
                precioProducto = float(input("Ingrese precio del producto: "))
                if precioProducto < 0:
                    print("Ingrese un numero positivo, por favor")
                    continue
            except ValueError:
                print("Ingrese un numero, por favor")
                continue
            else:
                break


        lista[i] = tdaProducto(codigo, cantidadStock, precioProducto)
        print(f' Producto {listaProductos[i]} cargado')
        contador += 1
        if contador < cantElementos:
            flag = input("Seguir cargando  productos: S/N ")
            if flag.upper() == "S":
                continue
            else:
                break
    return contador

def calcularProductoConMasStock(lista, contador):
    if contador == 0:
        return None
    else:
        indiceMax = 0
        for i in range(1, contador, 1):
            if lista[i].obtenerStock() > lista[indiceMax].obtenerStock():
                indiceMax = i
        return lista[indiceMax]


listaProductos = [0]*5
cantElementos = len(listaProductos)

contadorProducto = -1
opcion = -1
while opcion != 3:
    print("1. Cargar productos")
    print("2. Informar producto con mas stock")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        contadorProducto = cargaListaProductos(listaProductos, cantElementos)
    elif opcion == 2:
        productoMaxStock = calcularProductoConMasStock(listaProductos, contadorProducto)
        print(f'El producto con mas stock es: {productoMaxStock} y su cantidad es {productoMaxStock.obtenerStock()}')
    elif opcion == 3:
        break