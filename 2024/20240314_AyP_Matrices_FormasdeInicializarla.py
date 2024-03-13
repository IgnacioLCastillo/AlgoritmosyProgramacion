#Forma de inicializar una matriz con numpy
import numpy as np
#import random
#miMatrix = np.zeros(shape=(2,3),dtype=int)
# miMatrix = np.ones(shape=(2,3),dtype=int)
#miMatrix = np.full((2,3), random.randint(1,10))
#miMatrix = np.random.random((2,3))
#miMatrix = np.random.randint(1,10,(2,3))
#miMatrix = np.random.randint(1,10,(2,3))
#miMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.matrix('1 2 3; 4 5 6; 7 8 9')
#miMatrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.array([range(3),range(3)])
#miMatrix = np.matriz([range(3),range(3)])



#Formas Inicializar 1
matrix1 = np.zeros([2,3])
print ('Forma Inicializando 1',matrix1)

#Formas Inicializar 2
matrix1 = np.zeros(shape=(2,3))
print ('Forma 2 definiendo tamaño 2',matrix1)

#Formas Inicializar 1
matrix1 = np.matrix([range(3), range(3),range(3)])
print('Forma 1',matrix1)

#Formas Inicializar 2
matrix1 = np.matrix('1 2 3; 4 5 6; 7 8 9')
print ('Forma 2',matrix1)

#Formas Inicializar 3
matrix1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print ('Forma 3',matrix1)



matrix1 = np.array([[0,0,0],[0,0,0]])
print (matrix1)

matrix2 = np.zeros([2,3])
print (matrix2)

matrix3 = np.ones([2,3],dtype=int)
print (matrix3)

matrix4 = np.array([range(3),range(3)])
print ("range:",matrix4)

matrix5 = np.zeros(shape=(2,3),dtype=int)
print (matrix5)


A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)
A = np.array([[1, 2, 3], [3, 4, 5]], dtype = int)
print(A)
A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)

import numpy as np
matrix = np.array([[1.1, 2, 3], [3, 4, 5]])

filas=len(matrix)
columnas=len(matrix[0])
for i in range(0,filas,1):
    for j in range(0, columnas, 1):
        print("Elemento:",matrix[i][j])



'''
print ('Tama',matrix1.shape)
print ('Filas',len(matrix1))
print ('Columnas',len(matrix1[0]))
'''