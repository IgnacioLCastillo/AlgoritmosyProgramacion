#Creamos los nodos de la lista simplemente enlazada
class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.sig = None

#Damos valores a los nodos
varNodo1= Nodo('Valor 1')
varNodo2= Nodo('Valor 2')
varNodo3= Nodo('Valor 3')

#Enlazamos los nodos
varNodo1.sig = varNodo2
varNodo2.sig = varNodo3
varNodo3.sig = None

#Verificamos la informacion de los nodos
print(varNodo1.info)
print(varNodo1.sig.info)

