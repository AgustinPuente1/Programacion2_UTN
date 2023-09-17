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

print("Escribi 3 numeros enteros y positivos")
print("A B y X, se mostrara en pantalla los multiplos de X entre A y B")

A = input("A= ",)
A = esEntero(A)
A = esPositivo(A)

B = input("B= ",)
B = esEntero(B)
B = esPositivo(B)

X = input("X= ",)
X = esEntero(X)
X = esPositivo(X)

if(A > B):
    for i in range(B,A + 1):
        if ((i % X) == 0):
            print (i)

if(B > A):
    for i in range(A,B + 1):
        if ((i % X) == 0):
            print (i)

if(A == B):
    if((A % X) == 0):
        print(A)