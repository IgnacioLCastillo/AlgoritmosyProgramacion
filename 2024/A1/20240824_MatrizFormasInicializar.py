#Forma de inicializar una matriz con numpy
import numpy as np
import random
#miMatrix = np.zeros(shape=(2,3),dtype=int)
#miMatrix = np.ones(shape=(2,3),dtype=int)
#miMatrix = np.full((2,3), random.randint(1,10))
#miMatrix = np.random.random((2,3))
#miMatrix = np.random.randint(1,10,(2,3))
#miMatrix = np.random.randint(1,10,(2,3))
#miMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.matrix('1 2 3; 4 5 6; 7 8 9')
#miMatrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.array([range(3),range(3)])
#miMatrix = np.matriz([range(3),range(3)])
#print(miMatrix)

def udf_cargaMatriz(pmatriz,pran,pf,pc):
    for i in range(0,pf,1):
        for j in range(0,pc,1):
            if pran==1:
                pmatriz[i][j]=int(input(f'Ingrese Valor en miarreglo[{i}][{j}]:'))
            else:
                pmatriz[i][j]=random.randint(1,10)
    return pmatriz

def udf_muestraMatriz(pmatriz,pf,pc):
    for i in range(0,pf,1):
        print()
        for j in range(0,pc,1):
            print(f'[{i}][{j}]:{pmatriz[i][j]}',end='\t')
def udf_numeroImpares(pmatriz,pf,pc):
    for i in range(0,pf,1):
        print()
        for j in range(0,pc,1):
            if pmatriz[i][j]%2!=0:
                print(f'[{i}][{j}]:{pmatriz[i][j]}',end='\t')

def udf_minimoMatriz(pmatriz,pf,pc):
    minvalor=pmatriz[0][0]
    for i in range(0,pf,1):
        for j in range(0,pc,1):
            if pmatriz[i][j]<minvalor:
                minvalor=pmatriz[i][j]
    return minvalor

def udf_maximoParesMatriz(pmatriz,pf,pc):
    esPrimero=False
    maxvalor=0
    for i in range(0,pf,1):
        for j in range(0,pc,1):
            if pmatriz[i][j]%2==0:
                if esPrimero==False:
                    maxvalor=pmatriz[i][j]
                    esPrimero=True
                else:
                    if pmatriz[i][j]>maxvalor:
                        maxvalor=pmatriz[i][j]
    return maxvalor

def miMenu():
    print("")
    print('1. Cargar Datos Matriz')
    print('2. Carga random de Datos Matriz')
    print('3. Mostrar Datos de la Matriz')
    print('4. Numero Impares de Datos de la Matriz')
    print('5. Minimo de la Matriz')
    print('6. Maximo de los pares de la Matriz')
    print('7. Salir')
    opc = int(input('Ingrese Opcion:'))
    return opc



def udf_miMain():
    FILA=2
    COLUMNA=3
    miMatrix = np.zeros(shape=(FILA,COLUMNA),dtype=int)
    miMatrix2 = np.zeros(shape=(FILA, COLUMNA), dtype=int)
    #dibujoMenu
    opc=0
    while opc!=7:
        opc=miMenu()
        print('*' * 30)  # Dibuja 30 asteriscos#
        if opc==1:
            print("-CARGA NANUAL DE MATRIZ-")
            udf_cargaMatriz(miMatrix2, 1, FILA, COLUMNA)
        elif opc==2:
            print("-CARGA RANDOM-")
            udf_cargaMatriz(miMatrix,2,FILA,COLUMNA)
        elif opc==3:
            print("-MUESTRA MATRIZ RANDOM-")
            udf_muestraMatriz(miMatrix,FILA,COLUMNA)
            print("")
            print("-MUESTRA MATRIZ MANUAL-")
            udf_muestraMatriz(miMatrix2, FILA, COLUMNA)
        elif opc==4:
            print("-NUMEROS IMPARES DE LA MATRIZ RANDOM-")
            udf_numeroImpares(miMatrix,FILA,COLUMNA)
            print("")
            print("-NUMEROS IMPARES DE LA MATRIZ MANUAL-")
            udf_numeroImpares(miMatrix2, FILA, COLUMNA)
        elif opc==5:
            print("-MINIMO DE LA MATRIZ RANDOM-")
            print(udf_minimoMatriz(miMatrix2,FILA,COLUMNA))
            print("-MINIMO DE LA MATRIZ MANUAL-")
            print(udf_minimoMatriz(miMatrix,FILA,COLUMNA))
        elif opc==6:
            print("-MAXIMO DE LOS PARES DE LA MATRIZ RANDOM-")
            print(udf_maximoParesMatriz(miMatrix,FILA,COLUMNA))
            print("-MAXIMO DE LOS PARES DE LA MATRIZ MANUAL-")
            print(udf_maximoParesMatriz(miMatrix2, FILA, COLUMNA))
        elif opc==7:
            print('Termino el programa')
        else:
            print('Opcion no valida')
    print(miMatrix)


#************************************AreaGlobal****************************************************
udf_miMain()