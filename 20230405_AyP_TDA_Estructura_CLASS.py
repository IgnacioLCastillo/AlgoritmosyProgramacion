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
print(miEmpleado1)
print(miEmpleado2)

##Impresion de atriburos del registro Forma A
print("Empleado 1 Nombre:", tdaEMPLEADO.ObtenerNombre(miEmpleado1))
print("Empleado 1 Apellido:",tdaEMPLEADO.ObtenerApellido(miEmpleado1))
print("Empleado 2 Nombre:",tdaEMPLEADO.ObtenerNombre(miEmpleado2))
print("Empleado 2 Apellido:",tdaEMPLEADO.ObtenerApellido(miEmpleado2))

##Impresion de atriburos del registro Forma B
print(miEmpleado1.ObtenerNombre())
print(miEmpleado1.ObtenerApellido())
