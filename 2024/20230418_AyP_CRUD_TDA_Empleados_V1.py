#encoding: utf-8
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
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido

    def getSueldoBruto(self):
        return self.sueldo*.87

    def getSueldoNeto(self):
        return self.sueldo

    def getMaximoSueldo(self):

def udfBubbleSort(arrlistEmpleados):
    n = len(arrlistEmpleados)
    # optimizar el código, por lo que si la matriz ya está ordenada, no es necesario
    # para pasar por todo el proceso
    #hayCambios = False #Interruptor
    # Recorrer todos los elementos del arreglo o lista
    for pasada in range(n - 1):
        # range(n) también funciona, pero el bucle externo lo hará
        # repetir una vez más de lo necesario.
        # Los últimos elementos i ya están en su lugar
        EstaOrdenado = True #Interruptor asumiendo que esta ordenado. Es una hipotesis a refutar
        for j in range(0, n - pasada - 1):
            # recorrer el arreglo de 0 a n-i-1
            # Cambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arrlistEmpleados[j] > arrlistEmpleados[j + 1]:
                EstaOrdenado = False #Interruptor demostrando que no esta ordenado y debere seguir iterando
                #arrlistEmpleados[j], arrlistEmpleados[j + 1] = arrlistEmpleados[j + 1], arrlistEmpleados[j]
                aux = arrlistEmpleados[j]
                arrlistEmpleados[j] = arrlistEmpleados[j + 1]
                arrlistEmpleados[j + 1] = aux

        if EstaOrdenado: #Si esta ordenado, salimos del bucle
            return




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
    viMax = plisEmpleados[0].getSueldoBruto()
    posEmp=0
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].getSueldoBruto() > viMax:
            viMax = plisEmpleados[i].getSueldoBruto()
            posEmp=i

    return posEmp


##Programa Principal
lisEmpleados=[0]*3 ##Una de las tantas formas que tiene la lista de inicializar valores predefinidos. Aca solo
#cargamos 3 empleados x ahora
viOpcion = -1

viCantElem=len(lisEmpleados)
print(lisEmpleados)
while viOpcion != 8:
    print('\n')
    print('1-Carga Empleado')
    print('2-Retornar Sueldo Neto (Sueldo x.87)')
    print('3-Promedio Sueldo de Empleados')
    print('4-Mejor Sueldo')
    print('5-Mostrar Todos')
    print('6-Buscar Empleado por ID Legajo')
    print('7-Ordenar Empleado x Sueldo')
    print('8-Elimina Empleado')
    print('9-Actualiza Datos Empleado')
    print('10-Salir')
    viOpcion = int(input("Seleccione:"))

    if viOpcion==1:
        print("--------------Carga Empleados--------------")
        udfCargaEmpleados(lisEmpleados,viCantElem)
    elif viOpcion == 2:
        for cadaEmpleado in lisEmpleados: #Iteramos directamente sobre la coleccion
            print("--------------Seccion Sueldos Brutos--------------")
            print(f'Apellido:{cadaEmpleado.getApellido()} Sueldo Bruto:{cadaEmpleado.getSueldoBruto()}')
    elif viOpcion == 3:
        viSuma = 0
        for cadaEmpleado in lisEmpleados:
            print("--------------Promedio Empleados--------------")
            viSuma += cadaEmpleado.getSueldoBruto()

        print(f"El Promedio de todos los Empleados es:{float(viSuma/viCantElem)}")
    elif viOpcion == 4:
        print("--------------Empleado que mas Gana--------------")
        viMaxEmp=udfObtenerEmpMaximo(lisEmpleados, viCantElem)
        print(f'Apellido:{lisEmpleados[viMaxEmp].getApellido()} Sueldo Bruto:{lisEmpleados[viMaxEmp].getSueldoBruto()}')
    elif viOpcion == 5:
        print("--------------Mostrar Todos --------------")
    elif viOpcion == 6:
        print("--------------Buscar Secuencual Empleados--------------")
    elif viOpcion == 7:
        print("--------------Ordenar Empleados--------------")
    elif viOpcion == 8:
        print("--------------Eliminar Empleados--------------")
    elif viOpcion == 9:
        print("--------------Actualizar Empleados--------------")
    else:
        print('Error')