import pandas as pd
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

    def setNombre(self,pNombre):
        self.nombre=pNombre
        return self.nombre

    def getidLegajo(self):
        return self.idLegajo
    ##Retorno En Funciones
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido

    def getSueldoBruto(self):
        return self.sueldo

    def getSueldoNeto(self):
        return self.sueldo*.87


def udfMaxId(plisEmpleados, piCantElem):
    if len(plisEmpleados)>0:
        viMax = plisEmpleados[0].getidLegajo()
        for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
            if plisEmpleados[i].getidLegajo() > viMax:
                viMax = plisEmpleados[i].getidLegajo()
        return viMax+1
    else:
        return 1


def udfCargaEmpleados (plisEmpleados,piTopeCantElem,plOrdenStatus,piCantEmp=0):
    #for i in range(0,piCantElem,1):
    #piCantElem es el Tope de la lista
    vlFinaliza=False
    #es menor porque si pide 3 elemento va de 0 a 2
    while piCantEmp<piTopeCantElem and not vlFinaliza:
        print(f"Empleado {piCantEmp + 1} / {piTopeCantElem}")
        vinIdLegajo = udfMaxId(plisEmpleados, piCantEmp)
        vsNombre = input("Ingrese Nombre:")
        vsApellido = input("Ingrese Apellido:")
        # viEdad = int(input("Ingrese Edad:")) #Esto lo deje asi para que vaya el default a la funcion y vean como se maneja
        while True:
            try:
                vfSueldo = float(input("Ingrese el Sueldo:"))
                if vfSueldo < 0:
                    print("El numero debe ser positivo")
                    continue
            except ValueError:  #
                print("Error, Ingrese un numero")
                continue
            else:
                print(f"Advertencia - No se pueden argegar mas de {piTopeCantElem}")
                break
        # plisEmpleados[piCantEmp]=tdaEMPLEADO(vinIdLegajo,vsNombre, vsApellido,vfSueldo)
        plisEmpleados.append(tdaEMPLEADO(vinIdLegajo, vsNombre, vsApellido, vfSueldo))
        print (f' --------Empleado {plisEmpleados[piCantEmp]} --- Cargado con Exito ')
        '''
        with open("Empleados.txt", "a") as fileEmpleados:
            fileEmpleados.write(str(plisEmpleados[piCantEmp])+'-'+time.strftime("%c")+'\n')
        '''
        piCantEmp += 1
        vcContinua=input("Continua el Ingreso (S/N): ")
        if vcContinua.upper()=='N':
            vlFinaliza=True
    else:
        print("Lista Completa")

    return piCantEmp


def udfObtenerEmpMaximo(plisEmpleados,piCantElem):
    viMax = plisEmpleados[0].getSueldoBruto()
    posEmp=0
    print(piCantElem)
    for i in range(1, piCantElem, 1):  # Iteramos sobre cada elemento modalidad Arreglo.
        if plisEmpleados[i].getSueldoBruto() > viMax:
            viMax = plisEmpleados[i].getSueldoBruto()
            posEmp=i

    return posEmp


def udfMostrarTodos(plisEmpleados):
    #Esto lo hice porque use pandas. Me ayuda a dibijar mejor la tabla
    #Pero no es impresindible. Podemos mostrar con print simples.
    df = pd.DataFrame([vars(empleado) for empleado in plisEmpleados])
    print(df)

def udfBusquedaSecuencial(unaLista, item):
    pos = 0
    while pos < len(unaLista):
        if unaLista[pos].getidLegajo() == item:
            return pos
        else:
            pos = pos+1
    return -1



def udfBusquedaBinaria(lista, x):
    izq = 0 # izq guarda el indice inicio del segmento
    der = len(lista) -1 # der guarda el indice fin del segmento
    while izq <= der:
        medio =int((izq+der)/2)
        # Esta linea se habilita solo si quieren ver como se va moviendo el segmento izq, der y como maraca el medio
        #print ("DEBUG:", "izq:", izq, "der:", der, "medio:", medio) 
        if lista[medio].getidLegajo() == x:
            return medio
        elif lista[medio].getidLegajo() > x:
            der = medio-1
        else:
            izq = medio+1
    return -1


def udf_modificar_estudiante(listaestudiantes, indice, nuevo_nombre):
    unestudiante = listaestudiantes[indice]
    unestudiante.setNombre(nuevo_nombre)



def udfBubbleSortId(arr):
    n = len(arr)
    for i in range(n - 1):
        hayCambios = False
        for j in range(0, n - i - 1):
            if arr[j].getidLegajo() > arr[j + 1].getidLegajo():
                hayCambios = True
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
        if not hayCambios:
            return


def udfBubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        hayCambios = False
        for j in range(0, n - i - 1):
            if arr[j].getSueldoNeto() > arr[j + 1].getSueldoNeto():
                hayCambios = True
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
        if not hayCambios:
            return


##Programa Principal
def udf_mimain():
    viTopeLista=int(input("Defina el tope de Empleados a Cargar:"))
    lisEmpleados=[] ##Lista vacia
    viOpcion = -1
    viCantCargados=0
    #viCantElem=len(lisEmpleados)
    print(lisEmpleados)

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
        while True:
            try:
                viOpcion=int(input("Seleccione:"))
            except ValueError:
                print("Solo Admite numeros")
                continue
            else:
                break

        if viOpcion==1:
            print("--------------Carga Empleados--------------")
            if viCantCargados<viTopeLista:
                viCantCargados=udfCargaEmpleados(lisEmpleados,viTopeLista,viCantCargados)
            else:
                print (f"Lista llena- No se pueden argegar mas de {viTopeLista}")
                continue
        elif viOpcion == 2:
            for cadaEmpleado in lisEmpleados: #Iteramos directamente sobre la coleccion
                print("--------------Seccion Sueldos Brutos--------------")
                print(f'Apellido:{cadaEmpleado.getApellido()} Sueldo Bruto:{cadaEmpleado.getSueldoBruto()}')
        elif viOpcion == 3:
            viSuma = 0
            for cadaEmpleado in lisEmpleados:
                print("--------------Promedio Empleados--------------")
                viSuma += cadaEmpleado.getSueldoBruto()
            print(f"El Promedio de todos los Empleados es:{float(viSuma/(viCantCargados))}")
        elif viOpcion == 4:
            viMaxEmp=udfObtenerEmpMaximo(lisEmpleados, viCantCargados)
            print(f'Apellido:{lisEmpleados[viMaxEmp].getApellido()} Sueldo Bruto:{lisEmpleados[viMaxEmp].getSueldoBruto()}')
        elif viOpcion == 5:
            print("--------------Mostrar Todos --------------")
            udfMostrarTodos(lisEmpleados)
        elif viOpcion == 6:
            udfBubbleSortId(lisEmpleados)
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
                nuevoNombre = input("Ingrese el nuevo Nombre:")
                udf_modificar_estudiante(lisEmpleados,encontrado,nuevoNombre)
                print("Modificado con Exito")
                udfMostrarTodos(lisEmpleados)
        else:
            print('Error')

#AREA GLOBAL
udf_mimain()
