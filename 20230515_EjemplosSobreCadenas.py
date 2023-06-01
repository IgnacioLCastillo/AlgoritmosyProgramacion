
string = "\tHello, how are you\n"
print("Old String:")
print("'" + string + "'")

string = string.strip('\n')
string = string.strip('\t')
print("New String:")
print("'" + string + "'")

string = "Hello, \nhow are you\t?\n"
print("Old String:")
print("'" + string + "'")

string = string.replace('\n',"")
string = string.replace('\t',"")
print("New String:")
print("'" + string + "'")


print('1,2,3'.split(sep=','))
#['1', '2', '3']

print('  Me    gusta \t\nPython     '.split())
#['Me', 'gusta', 'Python']

'''
archivo = open("archivo.txt","r")
i = 1

for linea in archivo:
    linea = linea.rstrip("\n")
    #La llamada a rstrip es necesaria ya que cada linea que se lee del archivo contiene un fin de linea y lo remueve
    # y con la llamada a rstrip("\\n") se remueve.
    print ("%4d: %s" % (i, linea))
    i+=1
archivo.close()
'''