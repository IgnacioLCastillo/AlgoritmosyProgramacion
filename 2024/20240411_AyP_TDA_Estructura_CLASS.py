# TDA EMPLEADO
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

##Programa Principal
Num1=1
Num2=5
miEmpleado1 = tdaEMPLEADO("Jose", "Castro", "243434", 15)
miEmpleado2 = tdaEMPLEADO("Lucia","Martinez","111434", 22)
miEmpleado3 =tdaEMPLEADO("Roberto","Risotti","434", 23)

##Impresion de atriburos del registro Forma A
print("Forma 1 - Empleado 1 Nombre:", tdaEMPLEADO.ObtenerNombre(miEmpleado1))
print("Forma 1 - Empleado 1 Apellido:",tdaEMPLEADO.ObtenerApellido(miEmpleado1))
print("Forma 1 - Empleado 2 Nombre:",tdaEMPLEADO.ObtenerNombre(miEmpleado2))
print("Forma 1 - Empleado 2 Apellido:",tdaEMPLEADO.ObtenerApellido(miEmpleado2))
print("Forma 1 - Empleado 2 Nombre:",tdaEMPLEADO.ObtenerNombre(miEmpleado3))
print("Forma 1 - Empleado 2 Apellido:",tdaEMPLEADO.ObtenerApellido(miEmpleado3))

##Impresion de atriburos del registro Forma B
print('Forma 2 - ',miEmpleado1.ObtenerNombre())
print('Forma 2 - ',miEmpleado1.ObtenerApellido())
print('Forma 2 - ',miEmpleado2.ObtenerNombre())
print('Forma 2 - ',miEmpleado2.ObtenerApellido())
print('Forma 2 - ',miEmpleado3.ObtenerNombre())
print('Forma 2 - ',miEmpleado3.ObtenerApellido())