 #Definicion y dimensionamiento
import array as arr

def udfCargaVector(mipArreglo, vipCantElem):
    for i in range(0,vipCantElem,1):
        mipArreglo[i]=int(input("Ingrese un valor"))

def udfMiMaximo(mipArreglo, vipCantElem):
    lmax=mipArreglo[0]  #Asigno al primero como Maximo (y minimo si fuese el caso)
    for i in range(1, vipCantElem, 1):
            if mipArreglo[i]>lmax:
                lmax = mipArreglo[i]
    return lmax

def udfMuestraMatriz(mipArreglo, vipCantElem):
    #Muestro lo cargado
    for i in range(0, vipCantElem, 1):
        print(mipArreglo[i])


#----------------Main () del C-------------
miArreglo = arr.array('i',range(5))
miOtroArreglo= arr.array('i',range(8))
viCantElem=len(miArreglo)
viCantElemdelOtroArreglo=len(miOtroArreglo)
#Cargo El Vector
udfCargaVector(miArreglo,viCantElem)
maxResultado=udfMiMaximo(miArreglo,viCantElem)
udfMuestraMatriz(miArreglo,viCantElem)
print(f'El maximo es:{maxResultado}')

udfCargaVector(miOtroArreglo,viCantElemdelOtroArreglo)
maxResultado=udfMiMaximo(miOtroArreglo,viCantElemdelOtroArreglo)
udfMuestraMatriz(miOtroArreglo,viCantElemdelOtroArreglo)
print(f'El maximo es:{maxResultado}')
#udfCargaVector(miOtroArreglo,viCantElemdelOtroArreglo)



#Reviso el Maximo y lo muestro
'''for i in range(0, 5, 1):
    if i==0:
        max=miArreglo[i]
    else:
        if miArreglo[i]>max:
            max = miArreglo[i]
print(f"El maximo del vecto es {max} ")
'''