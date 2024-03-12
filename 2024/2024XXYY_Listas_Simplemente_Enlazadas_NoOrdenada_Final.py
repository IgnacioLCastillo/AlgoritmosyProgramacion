# -*- coding: utf-8 -*-
class Nodo:
    #Constructor de la clase Nodo
    def __init__(self, valor):
        self.info = valor
        self.sig = None
    def setValor(self, valor):
        self.info = valor
    def obtenerInfo(self):
        return self.info
    def obtenersig(self):
        return self.sig
    def asignarsig(self, nuevo_sig):
        self.sig = nuevo_sig

class ListaEnlazadaNoOrdenada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def mySize(self):
        return self.tamanio

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_nodo_posicion(self, nodo, posicion):
        if posicion == 0:
            nodo.sig = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            i = 0
            while actual and i < posicion:
                actual = actual.obtenersig()
                i += 1
            if not actual:
                raise ValueError("Posicion fuera de rango")
            nodo.sig = actual.obtenersig()
            actual.asignarsig(nodo)

    def agregar_nodo_alinicio(self, new_nodo):
        if self.esta_vacia():
            self.cabeza = new_nodo
            self.tamanio = 1
        else:
            new_nodo.sig = self.cabeza
            self.cabeza = new_nodo
            self.tamanio = self.tamanio + 1

    def agregar_nodo_alfinal(self, new_nodo):
        if self.esta_vacia():
            self.cabeza = new_nodo
            self.tamanio = 1
        else:
            actual = self.cabeza
            #while actual.sig:
            while actual.obtenersig() is not None:
                #actual = actual.sig
                actual = actual.obtenersig()
            #actual.sig = new_nodo
            actual.asignarsig(new_nodo)
            self.tamanio = self.tamanio + 1

        def buscar_nodo(self, valor):
            actual = self.cabeza
            encontrado = False
            while actual is not None and not encontrado:
                if actual.obtenerInfo() == valor:
                    encontrado = True
                else:
                    actual = actual.obtenersig()
            return encontrado

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.obtenerInfo(), end=" -> ")
            #podria acceder al atributo info de la siguiente manera:
            #print(actual.info, end=" -> ")
            actual = actual.sig
        print("None")

    def tamañoLista(self):
        actual = self.cabeza
        contador = 0
        while actual!=None:
            contador += 1
            actual = actual.sig
        return contador

    def eliminar_nodo(self, valor):
        actual = self.cabeza
        previo = None
        encontrado = False
        while actual is not None and not encontrado:
            if actual.obtenerInfo() == valor:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenersig()
        if encontrado == False:
            raise ValueError("El valor no se encuentra en la lista")
        else:
            self.tamanio = self.tamanio - 1
            if previo is None:
                self.cabeza = actual.obtenersig()
            else:
                previo.asignarsig(actual.obtenersig())
                # previo.sig = actual.sig


def mimenu():
    print("1. Agregar nodo al inicio")
    print("2. Agregar nodo al final")
    print("3. Mostrar lista")
    print("4. Buscar nodo")
    print("5. Tamaño de la lista")
    print("6. Eliminar nodo")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def mimain():
    miLista = ListaEnlazadaNoOrdenada()
    while True:
        opcionElegida = mimenu()
        if opcionElegida == 1:
            mivalor= input("Ingrese el valor a agregar: ")
            miLista.agregar_nodo_alinicio(Nodo(mivalor))
            miLista.mostrar_lista()
            print(miLista.mySize())
        elif opcionElegida == 2:
            mivalor = input("Ingrese el valor a agregar: ")
            miLista.agregar_nodo_alfinal(Nodo(mivalor))
            miLista.mostrar_lista()
            print(miLista.mySize())
        elif opcionElegida ==3:
            miLista.mostrar_lista()
        elif opcionElegida == 4:
            valor = input("Ingrese el valor a buscar: ")
            if miLista.buscar_nodo(valor):
                print("El valor se encuentra en la lista")
            else:
                print("El valor no se encuentra en la lista")
        elif opcionElegida == 5:
            print("El tamaño de la lista es: ", miLista.tamañoLista())
        elif opcionElegida == 6:
            valor = input("Ingrese el valor a eliminar: ")
            miLista.eliminar_nodo(valor)
            print(miLista.mySize())
        elif opcionElegida == 7:
            break
        else:
            print("Opcion incorrecta")

#Area global Ejecucion main
mimain()

