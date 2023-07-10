#Funciones

def myFunction(val):
    return val*val

print(myFunction(2))

a=[1,2,3]
def appendList (valor):

    print("Primer valor:" , a)
    a.append(valor)
    print("Despues de la funcion:",a)

appendList(4)