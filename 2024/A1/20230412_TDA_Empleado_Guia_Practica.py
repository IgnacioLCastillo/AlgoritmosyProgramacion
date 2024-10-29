class tdaEMPLEADO:
    def __init__(self, pID,pNombre, pApellido,pSueldo,pCategoria='P',pEdad=0):
        self.id = pID
        self.nombre = pNombre
        self.apellido = pApellido
        self.edad = pEdad
        self.categoria = pCategoria
        self.sueldo = pSueldo

   ##Retorno concatenado
    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def ObtenerCategoria(self):
        return self.categoria

    ##Retorno En Funciones
    def ObtenerNombre(self):
        return self.nombre

    def ObtenerID(self):
        return self.id

    def ObtenerApellido(self):
        return self.apellido

    def ObtenerSueldoNeto(self):
        return self.sueldo*.83

    def ObtenerSueldoBruto(self):
        return self.sueldo


def udfCargaEmpleados (plisEmpleados,piCantElem):

    for i in range(0,piCantElem,1):
        viID = i+1
        vsNombre=input("Ingrese Nombre:")
        vsApellido =input("Ingrese Apellido:")
        #viEdad = int(input("Ingrese Edad:"))

        while True:
            vcCategoria = input("Ingrese Categoria (T/P):")
            if vcCategoria.upper() == 'T' or vcCategoria.upper() == 'P':
                break
            else:
                print("debe Ingresar P(Planta) o T ( Temporal)")

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

        plisEmpleados[i]=tdaEMPLEADO(viID,vsNombre, vsApellido,vfSueldo,vcCategoria)
        print (f' --------Empleado {plisEmpleados[i]} --- Cargado con Exito ')




def udfMuestraEmpleados(plisEmpleados,piCantElem):

    '''for i in range (0,piCantElem,1):
        print(f"Apellido:{plisEmpleados[i].ObtenerNombre()}")
    '''

    for cadaEmpleado in plisEmpleados:  # Iteramos directamente sobre la coleccion
        print("--------------Seccion Sueldos Brutos--------------")
        print(f'ID: {cadaEmpleado.ObtenerID()} Nombre:{cadaEmpleado.ObtenerNombre()} Apellido:{cadaEmpleado.ObtenerApellido()} Categoria:{cadaEmpleado.ObtenerCategoria()} Sueldo Bruto:{cadaEmpleado.ObtenerSueldoBruto()}')

def udfPromedioxCategoria(plisEmpleados):
    viSumT =0
    viSumP =0
    viContT =0
    viContP = 0
    for cadaEmpleado in plisEmpleados:  # Iteramos directamente sobre la coleccion
        if cadaEmpleado.ObtenerCategoria()== 'T':
            viSumT+=cadaEmpleado.ObtenerSueldoBruto()
            viContT+=1
        elif cadaEmpleado.ObtenerCategoria()== 'P':
            viSumP  += cadaEmpleado.ObtenerSueldoBruto()
            viContP += 1

    return  float(viSumT/viContT), float(viSumP/viContP)



def udfObtenerEmpMaximo(plisEmpleados,piCantElem):
    viMax = plisEmpleados[0].ObtenerSueldoBruto()
    posEmp=0
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].ObtenerSueldoBruto() > viMax:
            viMax = plisEmpleados[i].ObtenerSueldoBruto()
            posEmp=i

    return posEmp


def udfObtenerEmpMinimo(plisEmpleados,piCantElem):
    viMin = plisEmpleados[0].ObtenerSueldoBruto()
    posEmp=0
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].ObtenerSueldoBruto() < viMin:
            viMin = plisEmpleados[i].ObtenerSueldoBruto()
            posEmp=i

    return posEmp





##------------------------------------Programa Principal-----------------------------------------
lisEmpleados=[0]*3 ##Una de las tantas formas que tiene la lista de inicializar valores predefinidos
viOpcion = -1

viCantElem=len(lisEmpleados)
print(lisEmpleados)
while viOpcion != 7:
    print('\n')
    print('1-Carga Empleado')
    print('2-Mostrar Todos los Empleados')
    print('3- Informar el empleado que mas y menos')
    print('4- Promemedio y cantidad x Categoria')
    print('7-Salir')
    viOpcion=int(input("Seleccione:"))
    if viOpcion==1:
        print("--------------Carga Empleados--------------")
        udfCargaEmpleados(lisEmpleados,viCantElem)
    elif viOpcion==2:
        udfMuestraEmpleados(lisEmpleados, viCantElem)
    elif viOpcion == 3:
        print("--------------Empleado que mas Gana--------------")
        viPosicMaximo = udfObtenerEmpMaximo(lisEmpleados, viCantElem)
        print(f"El que mas gana es :{lisEmpleados[viPosicMaximo].ObtenerNombre()} y su sueldo Neto es {lisEmpleados[viPosicMaximo].ObtenerSueldoNeto()}, Bruto:{lisEmpleados[viPosicMaximo].ObtenerSueldoBruto()} ")
        print("--------------Empleado que Menos Gana--------------")
        viPosicMinimo = udfObtenerEmpMinimo(lisEmpleados, viCantElem)
        print(f"El que mas gana es :{lisEmpleados[viPosicMinimo].ObtenerNombre()} y su sueldo Neto es {lisEmpleados[viPosicMinimo].ObtenerSueldoNeto()}, Bruto:{lisEmpleados[viPosicMinimo].ObtenerSueldoBruto()} ")
    elif viOpcion == 4:
        vfPromedioT,vfPromedioP = udfPromedioxCategoria(lisEmpleados)
        print(f"Promedio temporal es:{vfPromedioT}. Promedio Planta es: {vfPromedioP} ")
    elif viOpcion == 5:
        print('A Desarrollar')
    elif viOpcion == 6:
        print('A Desarrollar')
    elif viOpcion == 7:
        print('Fin del Algoritmo')
    else:
        print('Error')