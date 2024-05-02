##Programa Principal

class tdaProductos:
    def __init__(self,pCodigoProducto, pStock,pPrecio=0):
        self.codigo = pCodigoProducto
        self.stock = pStock
        self.precio = pPrecio

    def __str__(self):
        return str(self.codigo) + ' ' + str(self.stock) + ' ' + str(self.precio)


def udfMiMain():
    viTopeLista=5
    lisProductos=[0]*viTopeLista
    viOpcion = -1
    while viOpcion != 4:
        print('\n')
        print('1-Opcion 1')
        print('2-Opcion 2')
        print('3-Opcion 3')
        print('4-Salir')
        viOpcion=int(input("Seleccione:"))
        if viOpcion==1:
            print("--------------Opcion 1--------------")
        elif viOpcion == 2:
            print("--------------Opcion 2--------------")
        elif viOpcion == 3:
            print("--------------Opcion 3--------------")
        elif viOpcion == 4:
            print("--------------Salir--------------")
        else:
            print('Error')

#Programa Principal
udfMiMain()