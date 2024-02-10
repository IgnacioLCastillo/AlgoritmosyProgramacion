class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.sig = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo_desdeInicio(self, nodo):
        nodo.sig = self.cabeza
        self.cabeza = nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.sig
        print("None")


# Creamos la lista enlazada y agregamos los nodos
miLista = ListaEnlazada()
i=1
while i<=10:
    varNodo = Nodo(f'Valor {i}')
    miLista.agregar_nodo_desdeInicio(varNodo)
    i+=1


# Mostramos la lista enlazada
print("Lista Enlazada:")
miLista.mostrar_lista()