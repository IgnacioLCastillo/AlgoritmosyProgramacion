#Caso 1
try:
    suma=suma+2
except NameError:  # Variable desconocida
        print("Variable Desconocida")
#Caso 2
try:
    1/0
except ZeroDivisionError:  # Error en Division
        print("Division")

#Caso 3 *hay que poner un char para que falle)
try:
    viValor=int(input("Ingrese Valor"))
except ValueError:  # Variable desconocida
        print("Error. Debe ingresar un Entero")
