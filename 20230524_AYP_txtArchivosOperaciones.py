def udfMenu():
    print("1-Lectura Total")
    print("2-Conteo Lineas")
    print("3-Modificacion")
    print("4-Consulta")
    print("5-Busqueda")
    print("6-Salir")
    viOpcion=int(input("Ingrese Opcion:"))
    return viOpcion

def udfMuestraContenido():
    archivo = open("archivo.txt", "r")
    for linea in archivo:
        linea = linea.rstrip("\n")
        print(linea)

    archivo.close()


def udfConteoLineas():
    archivo = open("archivo.txt", "r")
    cantLinea = 0
    for linea in archivo:
        linea = linea.rstrip("\n")
        #La llamada a rstrip es necesaria ya que cada linea que se lee del archivo contiene un fin de linea
        # y con la llamada a rstrip("\\n") se remueve.
        print ("%4d: %s" % (cantLinea, linea))
        cantLinea+=1
    archivo.close()
    return cantLinea


def udfConteoPalabras():
    listaPalabras = []
    ##----Conteo de Palabras
    print ("*** 2 ***")

    #Con este enfoque, el archivo con el que esta trabajando se cierra automaticamente para que no tenga que acordarse de usar file.close().
    with open("archivo.txt", "r") as miArchivo:
        for lineas in miArchivo:
            listaPalabras.extend(lineas.split())
            print ("Contenido Lista:" , listaPalabras)

    cantPal = 0
    for unaPalabra in listaPalabras:
        print(unaPalabra)
        cantPal+=1

    return cantPal


def udfBusquedaLetra(pLetra):
    listaPalabras = []
    ##----Conteo de Palabras
    print ("*** 2 ***")
    cantPal=0
    with open("archivo.txt", "r") as fname:
        for lineas in fname:
                listaPalabras.extend(lineas.split())
                print ("Contenido Lista:" , listaPalabras)

    otraCant = 0
    for unaPalabra in listaPalabras:
        print(unaPalabra)
        tamPalabra=len(unaPalabra)
        for i in range(0,tamPalabra,1):
            if unaPalabra[i].upper() == pLetra:
                otraCant+=1

    return otraCant


#----------Programa Principal
viOpcionSele=-1
while  viOpcionSele!=7:
    viOpcionSele=udfMenu()
    if  viOpcionSele == 1:
        print("Lectura Total")
        udfMuestraContenido()
    elif viOpcionSele == 2:
        print("Cantidad Lineas:",udfConteoLineas())
    elif viOpcionSele == 3:
        print("Cantidad Palabras")
    elif viOpcionSele == 4:
        print("Cantidad Busqueda Letra")
    elif viOpcionSele == 5:
        print("Palabra mas grande")
    elif viOpcionSele == 6:
        print("Palabra Invertida")
    elif viOpcionSele == 7:
        print("Salir")
    else:
        print("Opcion Invalida")


resultado=udfConteoPalabras()

#print (datos2)
#print(len(datos2))
print(resultado)
print ("***")