import numpy as np

def udfParteInfContraDiagonal(pmatrix, pfilas,pColumnas):
    #misuma=0
    sosElprimero=True
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            if i+j>=(pfilas-1): #2 Elijo filas pero podria ser columna xq los dos valen igual
                print(pmatrix[i][j])
                if  pmatrix[i][j]%2==0: #Si es par y estoy en la zona
                    if sosElprimero==True:
                        max=pmatrix[i][j]
                        sosElprimero=False
                    else:
                        if pmatrix[i][j]>max:
                            max = pmatrix[i][j]

    return max


def udfSumaDiagonalPrincipal(pmatrix, pfilas,pColumnas):
    misuma=0
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            if i==j:
                misuma = misuma+pmatrix[i][j]

    return misuma

def udfImpParteSupDiagonalPrincipal(pmatrix, pfilas,pColumnas,pIncluye=False):
    conteoImp=0
    misumaImp=0
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            if pIncluye==True: #Incluye o no la diagonal. (sutil el tema de < o <=)
                if i<=j: #Incluye
                    if pmatrix[i][j]%2!=0:
                        misumaImp = misumaImp+pmatrix[i][j]
                        conteoImp+=1
            else:
                if i<j: #No la incluye
                    if pmatrix[i][j]%2!=0:
                        misumaImp = misumaImp+pmatrix[i][j]
                        conteoImp+=1

    return misumaImp/conteoImp


def udfSumaCDiagonal(pmatrix, pLargoDiag):
    i=0
    j=pLargoDiag-1 #Es como mandar 2 y tmb podria haber mandado columna, pero los dos tienen el mismo valor
    miSuma=0
    while j>=0:
        print(pmatrix[i][j])
        miSuma=miSuma+pmatrix[i][j]
        i+=1
        j=j-1
    return miSuma

def udfSumaCDiagonalFOR(pmatrix, pLargoDiag):
    j=pLargoDiag-1
    miSuma=0
    for i in range(0,pLargoDiag,1):
        print(pmatrix[i][j])
        miSuma = miSuma + pmatrix[i][j]
        j = j - 1
    return miSuma

def udfSumaDiagonalPrincipalComprimida(pmatrix, pLargoDiag):
    misuma=0
    for i in range(0,pLargoDiag,1):
         misuma = misuma+pmatrix[i][i]

    return misuma

def cargaMatriz(pmatrix, pfilas,pColumnas):
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            pmatrix[i][j]=int(input("Ingrese Valor:"))

def MostrarMatriz(pmatrix, pfilas,pColumnas):
    for i in range(0,pfilas,1):
        print('\n')
        for j in range(0, pColumnas, 1):
            print(f'({i},{j}):',pmatrix[i][j],end=' | ')
#*---------------
miMatrix = np.zeros(shape=(3,3),dtype=int)
filas=len(miMatrix)
columnas=len(miMatrix[0])
#print(miMatrix)

viOpcion=-1 #Global
while viOpcion!=6:
    print('\n')
    print('1-Suma Diagonal Principal')
    print('2-Suma Contra Diagonal')
    print('3-Promedio Impares Parte Sup. Diag. Princ')
    print('4-Parte Inferior Contra Diagonal')
    print('5-Cargar y muestra la matriz')
    print('6-Salir')
    viOpcion=int(input("Seleccione:"))

    if viOpcion==1:
        resultado = udfSumaDiagonalPrincipal(miMatrix, filas, columnas)
        print(resultado)
    elif viOpcion == 2:
        print(f"El resultado de la contra Diagonal (WHILE) es: {udfSumaCDiagonal(miMatrix, filas)}")
        print(f"El resultado de la contra Diagonal (FOR) es: {udfSumaCDiagonalFOR(miMatrix, filas)}")
    elif viOpcion == 3:

        while True:
            miEleccion=input("Incluye Diagonal S/N:")
            if miEleccion.upper()=='S':
                print(f"El promedio de los impares de la Parte sup Diagonal Principal (Incluye): {udfImpParteSupDiagonalPrincipal(miMatrix, filas,columnas,True)}")
                break;
            elif miEleccion.upper()=='N':
                print(f"El promedio de los impares de la Parte sup Diagonal Principal : {udfImpParteSupDiagonalPrincipal(miMatrix, filas,columnas)}")
                break
            else:
                print ('Error S/N')

    elif viOpcion == 4:
        maximoRecibido=udfParteInfContraDiagonal(miMatrix, filas, columnas)
        print('El maximo de los pares en la zona es:',maximoRecibido)
    elif viOpcion == 5:
        cargaMatriz(miMatrix, filas, columnas)
        MostrarMatriz(miMatrix, filas, columnas)
    elif viOpcion == 6:
        print('Salir')
    else:
        print('Incorrecto')
