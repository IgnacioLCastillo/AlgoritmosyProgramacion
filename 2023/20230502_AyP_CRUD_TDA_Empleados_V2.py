import time
# TDA EMPLEADO
class tdaEMPLEADO:
    def __init__(self,pLegajo, pNombre, pApellido,pSueldo,pEdad=0):
        self.idLegajo = pLegajo
        self.nombre = pNombre
        self.apellido = pApellido
        self.edad = pEdad
        self.sueldo = pSueldo

    ##Retorno concatenado
    def __str__(self):
        return 'Legajo: '+str(self.idLegajo)+'-Nombre y Apellido: '+self.nombre + ' ' + self.apellido+' Sueldo: '+str(self.sueldo)

    def ObteneridLegajo(self):
        return self.idLegajo
    ##Retorno En Funciones
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerApellido(self):
        return self.apellido

    def ObtenerSueldoBruto(self):
        return self.sueldo

    def ObtenerSueldoNeto(self):
        return self.sueldo*.87


def udfMaxId(plisEmpleados, piCantElem):
    if len(plisEmpleados)>0:
        viMax = plisEmpleados[0].ObteneridLegajo()
        for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
            if plisEmpleados[i].ObteneridLegajo() > viMax:
                viMax = plisEmpleados[i].ObteneridLegajo()
        return viMax+1
    else:
        return 1


def udfCargaEmpleados (plisEmpleados,piTopeCantElem,plOrdenStatus,piCantEmp=0):
    #for i in range(0,piCantElem,1):
    #piCantElem es el Tope de la lista
    vlFinaliza=False
    #es menor porque si pide 3 elemento va de 0 a 2
    while piCantEmp<piTopeCantElem and not vlFinaliza:
        print (f"Empleado {piCantEmp+1} / {piTopeCantElem}")

        vinIdLegajo=udfMaxId(plisEmpleados,piCantEmp)

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
                print(f"Lista llena- No se pueden argegar mas de {piTopeCantElem}")
                break



        #plisEmpleados[piCantEmp]=tdaEMPLEADO(vinIdLegajo,vsNombre, vsApellido,vfSueldo)
        plisEmpleados.append(tdaEMPLEADO(vinIdLegajo,vsNombre, vsApellido,vfSueldo))
        #print (plOrdenStatus, plisEmpleados[piCantEmp],vfSueldo)
        if vfSueldo < plisEmpleados[piCantEmp-1].ObtenerSueldoBruto() and plOrdenStatus == True:
            plOrdenStatus = False
        print (f' --------Empleado {plisEmpleados[piCantEmp]} --- Cargado con Exito ')
        with open("Empleados.txt", "a") as fileEmpleados:
            fileEmpleados.write(str(plisEmpleados[piCantEmp])+'-'+time.strftime("%c")+'\n')
        piCantEmp += 1
        vcContinua=input("Continua el Inrgeso (S/N): ")
        if vcContinua.upper()=='N':
            vlFinaliza=True

    else:
        print("Lista Completa")

    return piCantEmp,plOrdenStatus


def udfObtenerEmpMaximo(plisEmpleados,piCantElem):
    viMax = plisEmpleados[0].ObtenerSueldoBruto()
    posEmp=0
    print(piCantElem)
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].ObtenerSueldoBruto() > viMax:
            viMax = plisEmpleados[i].ObtenerSueldoBruto()
            posEmp=i

    return posEmp


def udfMostrarTodos(plisEmpleados):
    for cadaEmpleado in plisEmpleados:
        print(cadaEmpleado)


def udfBusquedaSecuencial(unaLista, item):
    pos = 0
    while pos < len(unaLista):
        if unaLista[pos].ObteneridLegajo() == item:
            return pos
        else:
            pos = pos+1
    return -1



def udfBusquedaBinaria(lista, x):
    izq = 0 # izq guarda el indice inicio del segmento
    der = len(lista) -1 # der guarda el indice fin del segmento
    while izq <= der:
        medio =int((izq+der)/2)
        print ("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)
        if lista[medio].ObteneridLegajo() == x:
            return medio
        elif lista[medio].ObteneridLegajo() > x:
            der = medio-1
        else:
            izq = medio+1
    return -1


def udf_modificar_estudiante(listaestudiantes, indice, nuevo_nombre):
    unestudiante = listaestudiantes[indice]
    unestudiante.nombre = nuevo_nombre



def udfBubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        hayCambios = False
        for j in range(0, n - i - 1):
            if arr[j].ObtenerSueldoNeto() > arr[j + 1].ObtenerSueldoNeto():
                hayCambios = True
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
        if not hayCambios:
            return


##Programa Principal

viTopeLista=int(input("Defina el tope de Empleados a Cargar:"))
lisEmpleados=[] ##Lista vacia
viOpcion = -1
viCantCargados=0
#viCantElem=len(lisEmpleados)
print(lisEmpleados)
vlEstaOrdenado=False
while viOpcion != 10:
    print('\n')
    print('1-Carga Empleado')
    print('2-Retornar Sueldo Neto (Sueldo x.87)')
    print('3-Promedio Sueldo de Empleados')
    print('4-Mejor Sueldo')
    print('5-Mostrar Todos')
    print('6-Buscar Empleado')
    print('7-Ordenar Empleado x Sueldo')
    print('8-Elimina Empleado')
    print('9-Actualiza Datos Empleado')
    print('10-Salir')
    viOpcion=int(input("Seleccione:"))

    if viOpcion==1:
        print("--------------Carga Empleados--------------")
        if viCantCargados<viTopeLista:
            viCantCargados,vlEstaOrdenado=udfCargaEmpleados(lisEmpleados,viTopeLista,vlEstaOrdenado,viCantCargados)
        else:
            print (f"Lista llena- No se pueden argegar mas de {viTopeLista}")
            continue
    elif viOpcion == 2:
        for cadaEmpleado in lisEmpleados: #Iteramos directamente sobre la coleccion
            print("--------------Seccion Sueldos Brutos--------------")
            print(f'Apellido:{cadaEmpleado.ObtenerApellido()} Sueldo Bruto:{cadaEmpleado.ObtenerSueldoBruto()}')
    elif viOpcion == 3:
        viSuma = 0
        for cadaEmpleado in lisEmpleados:
            print("--------------Promedio Empleados--------------")
            viSuma += cadaEmpleado.ObtenerSueldoBruto()

        print(f"El Promedio de todos los Empleados es:{float(viSuma/(viCantCargados))}")
    elif viOpcion == 4:
        viMaxEmp=udfObtenerEmpMaximo(lisEmpleados, (viCantCargados))
        print(f'Apellido:{lisEmpleados[viMaxEmp].ObtenerApellido()} Sueldo Bruto:{lisEmpleados[viMaxEmp].ObtenerSueldoBruto()}')
    elif viOpcion == 5:
        print("--------------Mostrar Todos --------------")
        udfMostrarTodos(lisEmpleados)
    elif viOpcion == 6:
        if not vlEstaOrdenado:
            print("La lista no esta ordenada")
        else:
            print("--------------Buscar Binaria Empleados--------------")
            while True:
                try:
                    idBuscado = int(input("Ingrese el ID a buscar:"))
                    if idBuscado < 0:
                        print("Id Empleado > a cero")
                        continue
                except ValueError:
                    print("Error, Solo acepta valores Numericos")
                    continue
                else:
                    break
            encontrado=udfBusquedaBinaria(lisEmpleados,idBuscado)
            if encontrado == -1:
                print(f"Empleado ID{idBuscado} no encontrado en la lista")
            else:
                print(lisEmpleados[encontrado])
    elif viOpcion == 7:
        print("--------------Ordenar Empleados--------------")

        udfBubbleSort(lisEmpleados)
        vlEstaOrdenado = True
        udfMostrarTodos(lisEmpleados)
    elif viOpcion == 8:
        print("--------------Elimina Empleado--------------")
        while True:
            try:
                idBuscado = int(input("Ingrese el ID a Eliminar:"))
                if idBuscado < 0:
                    print("Id Empleado > a cero")
                    continue
            except ValueError:
                print("Error, Solo acepta valores Numericos")
                continue
            else:
                break
        encontrado = udfBusquedaSecuencial(lisEmpleados, idBuscado)
        if encontrado == -1:
            print(f"Empleado ID{idBuscado} no encontrado en la lista")
        else:
            lisEmpleados.remove(lisEmpleados[encontrado])
            print("Eliminado con Exito")
            viCantCargados-=1
            udfMostrarTodos(lisEmpleados)

    elif viOpcion == 9:
        print("--------------Modificar Empleado--------------")
        while True:
            try:
                idBuscado = int(input("Ingrese el ID a Modificar:"))
                if idBuscado < 0:
                    print("Id Empleado > a cero")
                    continue
            except ValueError:
                print("Error, Solo acepta valores Numericos")
                continue
            else:
                break
        encontrado = udfBusquedaSecuencial(lisEmpleados, idBuscado)
        if encontrado == -1:
            print(f"Empleado ID{idBuscado} no encontrado en la lista")
        else:
            udf_modificar_estudiante(lisEmpleados,encontrado,"Juan")
            print("Modificado con Exito")
            udfMostrarTodos(lisEmpleados)



    else:
        print('Error')


