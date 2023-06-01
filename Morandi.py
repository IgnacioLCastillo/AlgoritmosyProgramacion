class TdaProducto:

    def __init__(self, codigo, stock, precio):
        self.codigoProducto = codigo
        self.stockProducto = stock
        self.precioProducto = precio
    ##Retorno concatenado
    def __str__(self):
        return str(self.codigoProducto)

    def obtenerPrecio(self):
        return self.precioProducto

    def obtenercodigoProducto(self):
        return self.codigoProducto

def cargarDatos(pproductos):

    for i in range(5):

        codigo = i + 1

        print(f"codigo del producto: {codigo}")

        while True:
            try:
                stock = int(input("ingrese el stock del producto: "))
                precio = float(input("ingrese el precio del producto: "))

                if stock < 0 or precio < 0:
                    print("El stock y el precio deben ser positivos")
                    continue
            except ValueError:  #
                print("Error, Ingreselos de nuevo")
                continue
            else:
                break
        pproductos[i] = TdaProducto(codigo, stock, precio)



def udfMuestraProductos(plisProductos):

    '''for i in range (0,piCantElem,1):
        print(f"Apellido:{plisEmpleados[i].ObtenerNombre()}")
    '''

    for cadaProducto in plisProductos:  # Iteramos directamente sobre la coleccion
        print("--------------Precios--------------")
        print(f'Precio: {cadaProducto.obtenerPrecio()} ID:{cadaProducto.obtenercodigoProducto()}')


def obtenerPrecioPromerio(pproductos):
    precioTotal = 0

    for producto in pproductos:
        precioTotal += producto.obtenerPrecio()

    promedio = precioTotal / len(pproductos)

    return float(promedio)


def mostrarPrecioPromedio(pproductos):
    promedio = obtenerPrecioPromerio(pproductos)
    print("Productos por encima del precio promedio: ")
    for producto in pproductos:
        if producto.obtenerPrecio() > promedio:
            print("Codigo: {}, Stock: {}, Precio: {}")



productos = [0] * 5
while True:

    print("Menu:")
    print("1. Cargar productos")
    print("2. Informar los productos que estan por encima del precio promedio")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        cargarDatos(productos)
        udfMuestraProductos(productos)

    elif opcion == 2:
        mostrarPrecioPromedio(productos)
    elif opcion == 3:
        break

    else:
        print("Opcion invalida")


