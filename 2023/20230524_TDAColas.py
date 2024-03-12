import numpy as np

def desplazarIzq(vector,fin):
    if fin < len(vector):
        for i in range(fin):
            vector[i] = vector[i+1]

class Cola:
    def __init__(self, tam, dtype = int):
        self.cola = np.zeros(shape = (tam), dtype=dtype)
        self.fin = None

    def isEmpty(self):
        return self.fin == None

    def isFull(self):
        return self.fin == len(self.cola)-1

    def queue(self, data):
        if self.isEmpty():
            self.fin = -1
        if not self.isFull():
            self.fin += 1
            self.cola[self.fin] = data
        else:
            raise Exception("No se pudo encolar el elemento "+str(data)+", la cola esta llena.")

    def dequeue(self):
        data = None
        if not self.isEmpty():
            data = self.cola[0]
            if self.fin == 0:
                self.fin = None
            else:
                desplazarIzq(self.cola,self.fin)
                self.fin -= 1
        else:
            raise Exception("No se puede obtener elemento de la cola. La cola esta vacia.")
        return data

    def top(self):
        data = None
        if not self.isEmpty():
            data = self.cola[0]
        else:
            raise Exception("No se puede obtener elemento de la cola. La cola esta vacia.")
        return data

    def clone(self):
        nueva = Cola(len(self.cola),self.cola.dtype)
        if not self.isEmpty():
            for i in range(self.fin+1):
                nueva.cola[i] = self.cola[i]
            nueva.fin = self.fin
        return nueva

    def getLen(self):
        clen = 0
        if not self.isEmpty():
            clen = self.fin + 1
        return clen

    def __repr__(self):
        outrepr = ""
        if not self.isEmpty():
            outrepr = ','.join([str(x) for x in self.cola[:self.fin+1]])
        else:
            outrepr = "La cola esta vacia."
        return outrepr

    def mostrar(self):
        mout = ""
        if not self.isEmpty():
            for i in range(self.fin+1):
                mout = mout + "," + str(self.cola[i])
            mout = mout[1:]
        else:
            mout = "La cola esta vacia."
        print(mout)


def main():
    cola1 = Cola(5, int)
    cola1.queue(3)
    cola1.queue(2)
    cola1.queue(4)
    cola1.queue(7)
    cola1.mostrar()
    print(cola1.dequeue())
    cola1.mostrar()
    cola2 = cola1.clone()
    print(cola2)


main()