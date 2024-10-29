# TDA EMPLEADO
class tdaEMPLEADO:
    def __init__(self,pId, pNombre, pApellido,pSueldo,pEdad=0):
        self.id = pId
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
        return 'Id:'+str(self.id)+' '+self.nombre + ' ' + self.apellido

    ##Retorno En Funciones
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido

    def getSueldoBruto(self):
        return self.sueldo

    def getSueldoNeto(self):
        return self.sueldo*.87
#----------------------------------------------------------

def udfCargaEmpleados (plisEmpleados,piCantElem):
    for i in range(0,piCantElem,1):
        vsNombre=input("Ingrese Nombre:")
        vsApellido =input("Ingrese Apellido:")
        viEdad = int(input("Ingrese Edad:"))
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

        plisEmpleados[i]=tdaEMPLEADO(i+1,vsNombre, vsApellido,vfSueldo,viEdad)
        print (f' --------Empleado {plisEmpleados[i]} --- Cargado con Exito ')


def udfObtenerEmpMaximo(plisEmpleados,piCantElem):
    viMax = plisEmpleados[0].getSueldoBruto()
    posEmp=0
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].getSueldoBruto() > viMax:
            viMax = plisEmpleados[i].getSueldoBruto()
            posEmp=i


    return posEmp



def mimainFuncion():
    viCantElem=int(input("Ingrese la cantidad de empleados: "))
    lisEmpleados=[0]*viCantElem ##Una de las tantas formas que tiene la lista de inicializar valores predefinidos
    viOpcion = -1
    print("Esto es solo para que vean como inicia la lista",lisEmpleados)
    while viOpcion != 8:
        print('\n')
        print('1-Carga Empleado')
        print('2-Retornar Sueldo Neto (Sueldo x.87')
        print('3-Promedio Sueldo de Empleados')
        print('4-Mejor y Peor Sueldo')
        print('5-Mostrar Todos')
        print('6-Buscar Empleado x')
        print('7-Ordenar Empleado (proximamente)')
        print('8-Salir')
        viOpcion=int(input("Seleccione:"))

        if viOpcion==1:
            print("--------------Carga Empleados--------------")
            udfCargaEmpleados(lisEmpleados,viCantElem)
        elif viOpcion == 2:
            for cadaEmpleado in lisEmpleados: #Iteramos directamente sobre la coleccion
                print("--------------Seccion Sueldos Brutos--------------")
                print(f'Apellido:{cadaEmpleado.getApellido()} Sueldo Bruto:{cadaEmpleado.getSueldoBruto()} de {cadaEmpleado.getSueldoNeto()}')
            ## Forma de iterar mas pareceida a como haciamos la iteracion de los vectore

            '''for i in range(0,viCantElem,1):
                print(lisEmpleados[i].getNombre())
                print(lisEmpleados[i].apellido) #Forma de acceder a los atributos. Accedo directo. No es recomendable, 
                # porque no oculta la implementacion de la clase.
            '''
        elif viOpcion == 4:
            viMaxEmp=udfObtenerEmpMaximo(lisEmpleados, viCantElem)
            print(f'Apellido:{lisEmpleados[viMaxEmp].getApellido()} Sueldo Bruto:{lisEmpleados[viMaxEmp].getSueldoBruto()}')
        elif viOpcion == 5:
            print("--------------Mostrar Todos --------------")
        elif viOpcion == 6:
            print("--------------Buscar Secuencual Empleados--------------")
        elif viOpcion == 7:
            print("--------------Ordenar Empleados--------------")
        else:
            print('Error')

# Programa Principal Area Global
mimainFuncion()