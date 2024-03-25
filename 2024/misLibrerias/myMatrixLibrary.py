def cargaMatriz(pmatrix, pfilas,pColumnas):
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            pmatrix[i][j]=int(input("Ingrese Valor:"))

def MostrarMatriz(pmatrix, pfilas,pColumnas):
    for i in range(0,pfilas,1):
        for j in range(0, pColumnas, 1):
            print(i,j,':',pmatrix[i][j])