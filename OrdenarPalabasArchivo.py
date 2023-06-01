#Realizar un algoritmo que permita la lectura de un archivo de texto y
# ordene mediante metodo de burbuja las palabras que contiene.
#

def udfOrdenamientoBurbuja(listaPalabras):
    aux = ""
    for i in range(0,len(listaPalabras)-1,1):
        for j in range(0,len(listaPalabras)-1,1):
            if listaPalabras[j] > listaPalabras[j+1]:
                aux = listaPalabras[j]
                listaPalabras[j] = listaPalabras[j+1]
                listaPalabras[j+1] = aux


def main():
    archivo = open("archivo.txt","r")
    i = 1
    listaPalabras = []
    for linea in archivo:
        linea = linea.rstrip("\n")
        #La llamada a rstrip es necesaria ya que cada linea que se lee del archivo contiene un fin de linea y lo remueve
        # y con la llamada a rstrip("\\n") se remueve.
        print ("%4d: %s" % (i, linea))
        listaPalabras.extend(linea.split())
        i+=1
    archivo.close()


    for palabra in listaPalabras:
        print(palabra)


    print ("Contenido Lista:" , listaPalabras)
    print("Cantidad de Palabras: ", len(listaPalabras))
    udfOrdenamientoBurbuja(listaPalabras)
    print ("Contenido Lista Ordenada:" , listaPalabras)

main()