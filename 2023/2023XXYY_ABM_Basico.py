class tdaEMPLEADO:
    def __init__(self, pNombre, pApellido, pDNI, pEdad):
        self.nombre = pNombre
        self.apellido = pApellido
        self.dni = pDNI
        if pEdad>0:
            self.edad = pEdad
        else:
            raise Exception ("la edad no puede ser negativa")
    ##Retorno concatenado
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    ##Retorno En Funciones
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerApellido(self):
        return self.apellido


def udfAltaEmpleado():

    vsNombre = input("Ingrese Nombre:")
    vsApellido = input("Ingrese Apellido:")
    vsDNI = input("Ingrese DNI:")
    viEdad = int(input("Ingrese Edad:"))
    with open('Empleados.bin', 'w') as filEmpleado:
    # write contents to the test2.txt file
        filEmpleado.write(tdaEMPLEADO(vsNombre, vsApellido, vsDNI, viEdad))


def udfMenu():
    print("1-Alta")
    print("2-Baja")
    print("3-Modificacion")
    print("4-Consulta")
    print("5-Busqueda")
    print("6-Salir")
    viOpcion=int(input("Ingrese Opcion:"))
    return viOpcion


#----------Programa Principal
viOpcionSele=-1
while  viOpcionSele!=6:
    viOpcionSele=udfMenu()
    if viOpcionSele==1:
        print("Alta")
        udfAltaEmpleado()


    elif viOpcionSele == 2:
        print("Baja")
    elif viOpcionSele == 3:
        print("Modificacion")
    elif viOpcionSele == 4:
        print("Consulta")
    elif viOpcionSele == 5:
        print("Busqueda")
    elif viOpcionSele == 6:
        print("Salir")
    else:
        print("Opcion Invalida")



