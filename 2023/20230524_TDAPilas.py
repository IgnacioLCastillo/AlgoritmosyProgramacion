import numpy as np

class Pila:
    def __init__(self, cap, dtype = int):
        self.pila = np.zeros(shape = (cap), dtype=dtype)
        self.cima = None

    def getType(self):
        return self.pila.dtype

    def isEmpty(self):
        empty = False
        if self.cima == None:
            empty = True
        return empty

    def isFull(self):
        full = False
        if self.cima == len(self.pila)-1:
            full = True
        return full

    def push(self, data):
        if self.isEmpty():
            self.cima = -1
        if not self.isFull():
            self.cima += 1
            self.pila[self.cima] = data
        else:
            print("No se pudo apilar el elemento "+str(data)+", la pila esta llena.")

    def pop(self):
        data = None
        if not self.isEmpty():
            data = self.pila[self.cima]
            if self.cima == 0:
                self.cima = None
            else:
                self.cima -= 1
        else:
            print("No se puede obtener elemento de la cima. La pila esta vacia.")
        return data

    def top(self):
        data = None
        if not self.isEmpty():
            data = self.pila[self.cima]
        else:
            print("No se puede obtener elemento de la cima. La pila esta vacia.")
        return data

    def empty(self):
        self.cima = None

    def getLen(self):
        tam = 0
        if not self.isEmpty():
            tam = self.cima+1
        return tam

    def clone(self):
        nueva = Pila(self.getLen(), self.pila.dtype)
        if not self.isEmpty():
            for i in range(self.cima+1):
                nueva.pila[i] = self.pila[i]
            nueva.cima = self.cima
        return nueva

    def clone2(self):
        nueva = Pila(self.getLen(), self.pila.dtype)
        if not self.isEmpty():
            for i in range(self.cima+1):
                nueva.push(self.pila[i])
        return nueva

    def mostrar(self):
        if not self.isEmpty():
            for i in range(self.cima+1):
                print(self.pila[i], ",", end="")
            print("")
        else:
            print("La pila esta vacia.")



Pila(5)
Pila.mostrar()