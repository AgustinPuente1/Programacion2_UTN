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

def perdirNrosBucle ():
    while True:    
        nro = input("Numero: ",)
        nro = esEntero(nro)
        nro = esPositivo(nro)

        if(nro == 0):
            break



print("Ingrese numeros enteros y positivos")
print("Finaliza con 0")

nro1 = input("Numero: ",)
nro1 = esEntero(nro1)
nro1 = esPositivo(nro1)

listaMayor = [nro1] 

while True: 
    nro2 = input("Numero: ",)
    nro2 = esEntero(nro2)
    nro2 = esPositivo(nro2)

    if (nro2 == 0):
        break

    listaMayor.append(nro2)

    if (listaMayor[0] <= listaMayor[1]):
        mayor = True 
    else: 
        mayor = False 
        perdirNrosBucle()
        break

    listaMayor.pop(0)

if(mayor == True):
    print("Los numeros estuvieron en orden")
else: 
    print("Los numeros no estuvieron en orden")

