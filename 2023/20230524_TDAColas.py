#encoding: utf-8
import numpy as np


def desplazarIzq(vector, fin):
    if fin < len(vector):
        for i in range(fin):
            vector[i] = vector[i + 1]


class Cola:
    def __init__(self, tam, dtype=int):
        self.cola = np.zeros(shape=(tam), dtype=dtype)
        self.fin = None

    def isEmpty(self):
        return self.fin == None

    def isFull(self):
        return self.fin == len(self.cola) - 1

    def queue(self, data):
        if self.isEmpty():
            self.fin = -1
        if not self.isFull():
            self.fin += 1
            self.cola[self.fin] = data
        else:
            raise Exception("No se pudo encolar el elemento " + str(data) + ", la cola está llena.")

    def dequeue(self):
        data = None
        if not self.isEmpty():
            data = self.cola[0]
            if self.fin == 0:
                self.fin = None
            else:
                desplazarIzq(self.cola, self.fin)
                self.fin -= 1
        else:
            raise Exception("No se puede obtener elemento de la cola. La cola está vacía.")
        return data

    def top(self):
        data = None
        if not self.isEmpty():
            data = self.cola[0]
        else:
            raise Exception("No se puede obtener elemento de la cola. La cola está vacía.")
        return data

    def clone(self):
        nueva = Cola(len(self.cola), self.cola.dtype)
        if not self.isEmpty():
            for i in range(self.fin + 1):
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
            outrepr = ','.join([str(x) for x in self.cola[:self.fin + 1]])
        else:
            outrepr = "La cola está vacía."
        return outrepr

    def mostrar(self):
        mout = ""
        if not self.isEmpty():
            for i in range(self.fin + 1):
                mout = mout + "," + str(self.cola[i])
            mout = mout[1:]
        else:
            mout = "La cola está vacía."
        print(mout)


def menu():
    print("----- Menú -----")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Mostrar elemento superior")
    print("4. Clonar cola")
    print("5. Mostrar cola")
    print("6. Salir")
    opcion = int(input("Ingrese su opción: "))
    return opcion


def main():
    tamCola = int(input("Ingrese el tamaño de la cola: "))
    cola = Cola(tamCola)

    while True:
        opcion = menu()

        if opcion == 1:
            valor = int(input("Ingrese el valor a encolar: "))
            cola.queue(valor)
            print("Elemento encolado.")
        elif opcion == 2:
            try:
                valor = cola.dequeue()
                print("Elemento desencolado:", valor)
            except Exception as e:
                print(e)
        elif opcion == 3:
            try:
                valor = cola.top()
                print("Elemento superior de la cola:", valor)
            except Exception as e:
                print(e)
        elif opcion == 4:
            colaClonada = cola.clone()
            print("Cola clonada:", colaClonada)
        elif opcion == 5:
            print("Contenido de la cola:", cola)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
