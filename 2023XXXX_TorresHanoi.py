
#https://www.youtube.com/watch?v=Ru6dBRtxNrM&t=525s

def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

moverTorre(4,"A","B","C")
