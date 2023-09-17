def esNumero (caracter):
    while True:
        try:
            caracter = float(caracter)
        except:
            caracter = input("Lo ingresado no es un número, ingrese uno: ")
            continue
        caracter = str(caracter)
        break
    return caracter

numero = input("Ingrese un número: ")
numero = esNumero(numero)

#pone cada caracter del numero en una lista por separado

listaNrosDivididos = []
for i in numero:
    if (i.isnumeric() == True):
        nroDividido = float(i)
        listaNrosDivididos.append(nroDividido)

#cual es el nro más alto y que indice tiene

nroHigher = 0
indicesNroHigher = []

for i in range(0,len(listaNrosDivididos)):
    if (nroHigher <= listaNrosDivididos[i]):
        nroHigher = listaNrosDivididos[i]


for i in range(0,len(listaNrosDivididos)):
    if (nroHigher == listaNrosDivididos[i]):
        indicesNroHigher.append(i)

#prints

print("El numero más alto de la cadena de numero ingresa es ",int(nroHigher))
print("En la posicion que esta/n es: ",end="")

for i in indicesNroHigher:
    print(i + 1, end=" ")
        