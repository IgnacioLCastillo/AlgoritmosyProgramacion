#Emeplo 1 - Mostrar como Iterar con for
'''
for i in range(0,5,1):
    viEdad=int(input("Ingrese la Edad"))
    vcSexo=input("Ingrese el Sexo")
    vfSueldo=float(input("Ingrese el Sueldo"))
    if viEdad >= 18 and vcSexo.upper() == 'F' and vfSueldo > 10000:
        print("Cumple con los requisitos")
    else:
        print("no los cumple")
'''

'''
# Ejemplo 2 - Emular Clave con while
viNroError=0
vcClave='Unpaz1234'
while viNroError < 3:
    vcClaveingresada= input("Ingrese la Clave:")
    if vcClave == vcClaveingresada:
        print("Clave Correcta")
        viNroError=3
    else:
        viNroError += 1
        print("Clave Incorrecta",viNroError)

'''

'''
#Ejemplo 3 - Emular Clave con do while / repeat until
viNroError=0
vcClave='Unpaz1234'
while True:
    vcClaveingresada= input("Ingrese la Clave:")
    if vcClave == vcClaveingresada:
        print("Clave Correcta")
        break
    else:
        viNroError += 1
        print("Clave Incorrecta",viNroError)
        print(f"Le quedan {3-viNroError} intentos")
        if viNroError == 3:
            break
'''

#Ejemplo 4 - Mostrar seleccion multiple
opcion=0
while opcion != 4:
    print("1- Ingresar")
    print("2- Modificar")
    print("3- Eliminar")
    print("4- Salir")
    opcion=int(input("Ingrese la opcion:"))
    '''
    if opcion == 1:
        print("Ingresar")
    elif opcion == 2:
        print("Modificar")
    elif opcion == 3:
        print("Eliminar")
    elif opcion == 4:
        print("Salir")
    else:
        print("Opcion Incorrecta")
    '''
    match opcion:
        case 1:
            print("Ingresar")
        case 2:
            print("Modificar")
        case 3:
            print("Eliminar")
        case 4:
            print("Salir")
        case _:
            print("Opcion Incorrecta")
