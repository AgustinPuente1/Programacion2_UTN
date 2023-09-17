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
        if (nro > 0):
            print("Tu nro es positivo y entero")
            break
        else:
            nro = input("El numero es 0 o negativo, escribi otro: ",)
            esEntero(int(nro))
    return (nro)

numero = input("Ingrese un numero positivo y entero: ",)
numero = esEntero(numero)
numero = esPositivo(numero)

for i in range(1,numero+1):
    print (i)
