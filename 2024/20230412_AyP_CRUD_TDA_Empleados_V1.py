# TDA EMPLEADO
class tdaEMPLEADO:
    def __init__(self, pNombre, pApellido,pSueldo,pEdad=0):
        self.nombre = pNombre
        self.apellido = pApellido
        if pEdad>=0:
            self.edad = pEdad
        else:
            raise Exception ("la edad no puede ser negativa")

        if pSueldo>0:
            self.sueldo = pSueldo
        else:
            raise Exception ("El Sueldo debe ser > 0 ")

    ##Retorno concatenado
    def __str__(self):
        return self.nombre + ' ' + self.apellido

    ##Retorno En Funciones
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerApellido(self):
        return self.apellido

    def ObtenerSueldoBruto(self):
        return self.sueldo*.87

    def ObtenerSueldoNeto(self):
        return self.sueldo


def udfCargaEmpleados (plisEmpleados,piCantElem):
    for i in range(0,piCantElem,1):
        vsNombre=input("Ingrese Nombre:")
        vsApellido =input("Ingrese Apellido:")
        #viEdad = int(input("Ingrese Edad:"))
        while True:
            try:
                vfSueldo=float(input("Ingrese el Sueldo:"))
                if vfSueldo<0:
                    print("El numero debe ser positivo")
                    continue
            except ValueError:  #
                print("Error, Ingrese un numero")
                continue
            else:
                break

        plisEmpleados[i]=tdaEMPLEADO(vsNombre, vsApellido,vfSueldo)
        print (f' --------Empleado {plisEmpleados[i]} --- Cargado con Exito ')


def udfObtenerEmpMaximo(plisEmpleados,piCantElem):
    viMax = plisEmpleados[0].ObtenerSueldoBruto()
    posEmp=0
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].ObtenerSueldoBruto() > viMax:
            viMax = plisEmpleados[i].ObtenerSueldoBruto()
            posEmp=i

    return posEmp


##Programa Principal
lisEmpleados=[0]*2 ##Una de las tantas formas que tiene la lista de inicializar valores predefinidos
viOpcion = -1

viCantElem=len(lisEmpleados)
print(lisEmpleados)
while viOpcion != 8:
    print('\n')
    print('1-Carga Empleado')
    print('2-Retornar Sueldo Neto (Sueldo x.87')
    print('3-Promedio Sueldo de Empleados')
    print('4-Mejor y Peor Sueldo')
    print('5-Mostrar Todos')
    print('6-Buscar Empleado')
    print('7-Ordenar Empleado')
    print('8-Salir')
    viOpcion=int(input("Seleccione:"))

    if viOpcion==1:
        print("--------------Carga Empleados--------------")
        udfCargaEmpleados(lisEmpleados,viCantElem)
    elif viOpcion == 2:
        for cadaEmpleado in lisEmpleados: #Iteramos directamente sobre la coleccion
            print("--------------Seccion Sueldos Brutos--------------")
            print(f'Apellido:{cadaEmpleado.ObtenerApellido()} Sueldo Bruto:{cadaEmpleado.ObtenerSueldoBruto()}')
    elif viOpcion == 3:
        viSuma = 0
        for cadaEmpleado in lisEmpleados:
            print("--------------Promedio Empleados--------------")
            viSuma += cadaEmpleado.ObtenerSueldoBruto()

        print(f"El Promedio de todos los Empleados es:{float(viSuma/viCantElem)}")
    elif viOpcion == 4:
        viMaxEmp=udfObtenerEmpMaximo(lisEmpleados, viCantElem)
        print(f'Apellido:{lisEmpleados[viMaxEmp].ObtenerApellido()} Sueldo Bruto:{lisEmpleados[viMaxEmp].ObtenerSueldoBruto()}')
    elif viOpcion == 5:
        print("--------------Mostrar Todos --------------")
    elif viOpcion == 6:
        print("--------------Buscar Secuencual Empleados--------------")
    elif viOpcion == 7:
        print("--------------Ordenar Empleados--------------")
    else:
        print('Error')