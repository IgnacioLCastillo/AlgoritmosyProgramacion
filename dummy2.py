class tdaProducto:

    def __init__(self, cod, stock, precio):
        self.codigo = cod
        self.cant_Stock = stock
        self.precio_Produc = precio

    def __str__(self):
        return self.codigo


def cargar_vector(vector):
    contador = 0
    for i in range(0, cantElement, 1):
        codigo = input("Ingrese el código del producto: ")
        while True:
            try:
                cant_Stock = int(input("Ingrese stock del producto: "))
                if cant_Stock < 0:
                    print("Ingrese un numero positivo, por favor")
                    continue
            except ValueError:
                print("Ingrese un numero, por favor")
                continue
            else:
                break
        while True:
            try:
                precio_Produc = float(input("Ingrese precio del producto: "))
                if precio_Produc < 0:
                    print("Ingrese un numero positivo, por favor")
                    continue
            except ValueError:
                print("Ingrese un numero, por favor")
                continue
            else:
                break
        vector.append(tdaProducto(codigo, cant_Stock, precio_Produc))
        if contador < cantElement:
            flag = input("Seguir cargando  productos: S/N ")
            if flag.upper() == "S":
                continue
            else:
                break
        contador += 1
        return contador

    print("Datos cargados correctamente")


def precio_promedio(vector):
    total_precios = sum([producto.precio_Produc for producto in vector])
    return total_precios / len(vector)


def productos_Encima_Del_Promedio(vector):
    promedio = precio_promedio(vector)
    print(f"Productos con precio por encima de ${promedio:.2f}:")
    for producto in vector:
        if producto.precio_Produc > promedio:
            print(f"- Código: {producto.codigo}, Stock: {producto.cant_stock}, Precio: ${producto.precio_Produc:.2f}")


vector = [0] * 5
cantElement = len(vector)


def menu(vector):
    while True:
        print("=== Menú ===")
        print("1) Cargar datos del vector")
        print("2) Mostrar productos por encima del precio promedio")
        print("3) Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cargar_vector(vector)
        elif opcion == "2":
            productos_Encima_Del_Promedio(vector)
        elif opcion == "3":
            break

        else:
            print("Opción inválida")


menu(vector)