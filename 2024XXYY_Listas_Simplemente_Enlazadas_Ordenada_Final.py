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

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def mySize(self):
        return self.tamanio

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_nodo_Ordenado(self, new_nodo):
        if self.esta_vacia():
            self.cabeza = new_nodo
            self.tamanio = 1
        else:
            actual = self.cabeza
            previo = None
            detenerse = False
            while actual!=None and not detenerse:
                if actual.obtenerInfo() > new_nodo.obtenerInfo():
                    detenerse = True
                else:
                    previo = actual
                    actual = actual.obtenersig()

            if previo is None:
                new_nodo.sig = self.cabeza
                self.cabeza = new_nodo
            else:
                new_nodo.sig = actual
                previo.sig = new_nodo
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
    print("1. Agregar nodo lista ordenada")
    print("3. Mostrar lista")
    print("4. Buscar nodo")
    print("5. Tamaño de la lista")
    print("6. Eliminar nodo")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion



def mimain():
    miLista = ListaEnlazadaOrdenada()
    while True:
        opcionElegida = mimenu()
        if opcionElegida == 1:
            mivalor= input("Ingrese el valor a agregar: ")
            miLista.agregar_nodo_Ordenado(Nodo(mivalor))
            miLista.mostrar_lista()
            print(miLista.mySize())
        elif opcionElegida ==2:
            miLista.mostrar_lista()
        elif opcionElegida == 3:
            valor = input("Ingrese el valor a buscar: ")
            if miLista.buscar_nodo(valor):
                print("El valor se encuentra en la lista")
            else:
                print("El valor no se encuentra en la lista")
        elif opcionElegida == 4:
            print("El tamaño de la lista es: ", miLista.tamañoLista())
        elif opcionElegida == 5:
            valor = input("Ingrese el valor a eliminar: ")
            miLista.eliminar_nodo(valor)
            print(miLista.mySize())
        elif opcionElegida == 6:
            break
        else:
            print("Opcion incorrecta")

#Area global Ejecucion main
mimain()