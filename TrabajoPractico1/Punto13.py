def esEntero (nro):
    while True:
        try:
            entero = int(nro)
        except ValueError:
            nro = input("No valido, ingrese otro numero: ",)
            continue
        break
    return nro

def esPositivo (nro):
    while True: 
        nro = int(nro)
        if (nro >= 0):
            print("Tu nro es positivo y entero")
            break
        else:
            nro = input("El numero es 0 o negativo, escribi otro: ",)
            esEntero(int(nro))
    return (nro)

caracter = input("Ingrese un caracter: ",)
cantRepeticiones = input("Ingrese la cantidad de repeticiones del caracter: ",)
cantRepeticiones = esEntero (cantRepeticiones)
cantRepeticiones = esPositivo (cantRepeticiones)


while (cantRepeticiones != 0): 
    print (caracter)
    cantRepeticiones -= 1
