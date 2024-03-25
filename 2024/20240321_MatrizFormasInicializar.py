#Forma de inicializar una matriz con numpy
import numpy as np
import random
#miMatrix = np.zeros(shape=(2,3),dtype=int)
#miMatrix = np.ones(shape=(2,3),dtype=int)
#miMatrix = np.full((2,3), random.randint(1,10))
#miMatrix = np.random.random((2,3))
#miMatrix = np.random.randint(1,10,(2,3))
miMatrix = np.random.randint(1,10,(2,3))
#miMatrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.matrix('1 2 3; 4 5 6; 7 8 9')
#miMatrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#miMatrix = np.array([range(3),range(3)])
#miMatrix = np.matriz([range(3),range(3)])
print(miMatrix)
