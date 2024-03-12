with open("Mitextobinario.bin", "wb") as archivo:
    texto=b"Argentina es tricampeon mundial.\n" #Aca lo paso a bit con el b
    archivo.write(texto)
    texto="pythön es tricampeón mundial." #Aca lo paso a bit con encode
    print('Resultado:',texto.encode('utf-8'))
    archivo.write(texto.encode('utf-8'))
