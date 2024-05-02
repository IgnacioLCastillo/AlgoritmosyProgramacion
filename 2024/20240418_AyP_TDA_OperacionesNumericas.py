# TDA OperacionesMatematicas
class tdaOperaciones:
    def __init__(self, pNumA, pNumB):
        self.numeroA = pNumA
        self.numeroB = pNumB

    ##Retorno concatenado
    def __str__(self):
        return str(self.numeroA) + ' ' + str(self.numeroB)

    ##Retorno En Funciones
    def ObtenerSuma(self):
        return self.numeroA+self.numeroB

    def ObtenerResta(self):
        return self.numeroA - self.numeroB

##Programa Principal
miSetNumerosA = tdaOperaciones(2,15)
miSetNumerosB = tdaOperaciones(22,15)
print(miSetNumerosA)
print(miSetNumerosA.ObtenerSuma())
print(tdaOperaciones.ObtenerResta(miSetNumerosB))
print(miSetNumerosB.ObtenerResta())


