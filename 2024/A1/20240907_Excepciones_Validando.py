import numpy as np

def udfCarga_Matriz (pMatriz,pFil,pCol):
    for i in range(0,pFil,1):
        for j in range(0, pCol, 1):
            while True:
                try:
                    viValor=int(input(f"Ingrese Valor {i}{j}:"))
                #except ValueError:  # Variable desconocida
                #    print("Error, Ingrese un numero")
                #    continue
                except Exception as e:
                    print("Error:",e)
                    continue
                if viValor < 0:
                    print("Debes escribir un numero positivo.")
                    #raise Exception("Sorry, no numbers below zero")
                    continue
                else:
                    break

            pMatriz[i][j]=viValor


#----------Principal
FILAS=3
COLUMNAS=2
#matrix = np.zeros([FILAS,COLUMNAS],dtype=int)
suma=11
otrovalor=int(input("Ingrese otro valor"))
print(otrovalor)
suma=suma+otrovalor
print(suma)
matrix = np.zeros(shape=(FILAS,COLUMNAS),dtype=int)
udfCarga_Matriz(matrix,FILAS,COLUMNAS)

print(matrix)







