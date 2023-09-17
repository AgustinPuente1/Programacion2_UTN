texto = input("Ingrese un texto: ")

listaCaracteres = [0]
nroCaracter = 0
largoPalabra = 0
x = int(0)
y = int(0)

for i in texto:    
    if (i == " "):
        listaCaracteres.append(nroCaracter)
    nroCaracter += 1

listaCaracteres.append(nroCaracter)
    
for i in range(0,len(listaCaracteres)):

    try:
        auxLargo = listaCaracteres[i + 1] - listaCaracteres[i]
    except IndexError:
         break
    
    if (auxLargo >= largoPalabra):
        if (i == 0):
            x = listaCaracteres[i]
        else:
            x = listaCaracteres[i] + 1
        
        y = listaCaracteres[i + 1]

        largoPalabra = auxLargo - 1
    
contador = 0
listaPalabra = []

for i in texto:
    if (contador >= x) and (contador < y):
            listaPalabra.append(i)
    contador += 1

print("La palabra más larga del texto es: ",end="")

for i in range(0,largoPalabra):
    print(listaPalabra[i],end="")
    
print ("\nLa palabra tiene %i letras" % (largoPalabra))