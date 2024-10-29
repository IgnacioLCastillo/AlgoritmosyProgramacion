def udf_mi_funcion(pnumeroA,pnumeroB,plista):
    plista[0]=99
    pResultado=pnumeroA+pnumeroB
    return pResultado

def udf_miMain():
    lista=[1,2,3,4,5]
    print(lista)
    numeroA=5
    numeroB=6
    print('Main:',numeroA)
    print('Main:',udf_mi_funcion(numeroA,numeroB,lista))
    print(lista)

#Areaglobal
udf_miMain()
