# TDA EMPLEADO
class tdaEMPLEADO:
    def __init__(self, pNombre, pApellido, pDNI, pEdad):
        self.nombre = pNombre
        self.apellido = pApellido
        self.dni = pDNI
        if pEdad>0:
                self.edad = pEdad
        else:
                #raise Exception ("la edad no puede ser negativa")
                self.edad = 0
                print ("la edad no puede ser negativa")
    ##Retorno concatenado
    def __str__(self):
        return self.nombre + 'XXXX' + self.apellido

    def set_dni(self, pDNI):
        self.dni = pDNI

    def set_edad(self, pEdad):
        self.edad = pEdad

    def get_dar_nombre_apellido(self):
        return self.nombre + ' ' + self.apellido
    ##Retorno En Funciones
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_dni(self):
        return self.dni
    def get_edad(self):
        return self.edad

##Programa Principal
miEmpleado1 = tdaEMPLEADO("Jose", "Castro", "243434", 15)
miEmpleado2 = tdaEMPLEADO("Lucia","Martinez","111434", 1)
print(miEmpleado1)
print(miEmpleado2)

##Impresion de atriburos del registro Forma A
print("Empleado 1 Nombre:", tdaEMPLEADO.get_nombre(miEmpleado1))
print("Empleado 1 Apellido:",tdaEMPLEADO.get_apellido(miEmpleado1))
print("Empleado 2 Nombre:",tdaEMPLEADO.get_nombre(miEmpleado2))
print("Empleado 2 Apellido:",tdaEMPLEADO.get_apellido(miEmpleado2))
print("Empleado 1 DNI:",tdaEMPLEADO.get_dni(miEmpleado1))
print("Empleado 2 DNI:",tdaEMPLEADO.get_dni(miEmpleado2))
print("Empleado 1 Edad:",tdaEMPLEADO.get_edad(miEmpleado1))
print("Empleado 2 Edad:",tdaEMPLEADO.get_edad(miEmpleado2))

##Impresion de atriburos del registro Forma B
print(miEmpleado1.get_nombre())
print(miEmpleado1.get_apellido())
print(miEmpleado1.get_edad())
print(miEmpleado1.edad)
#modificar edad directo
miEmpleado1.edad = 20
print(miEmpleado1.get_edad())

miEmpleado1.set_edad(30)
print(miEmpleado1.get_edad())
