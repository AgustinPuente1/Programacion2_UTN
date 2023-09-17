def esEntero (nro):
    while True:
        try:
            entero = int(nro)
        except ValueError:
            nro = input("No valido, ingrese un numero entero: ",)
            continue
        break
    return nro

def esPositivo (nro):
    while True: 
        nro = int(nro)
        if (nro > 0):
            break
        else:
            nro = input("El numero es 0 o negativo, escribi otro: ",)
            esEntero(int(nro))
    return nro

print("Ingrese la cantidad de notas que quiere ingresar, luego se le indicara cual es la nota más alta")

cantNotas = input("Cantidad de notas que quiera ingresar: ")
cantNotas = esEntero(cantNotas)
cantNotas = esPositivo(cantNotas)

#almacena las notas en una lista
listaNotas = []
for i in range(0,cantNotas):
    nuevaNota = input("")
    nuevaNota = esEntero(nuevaNota)
    nuevaNota = esPositivo(nuevaNota)
    listaNotas.append(nuevaNota)

#calcula cual es la nota más alta y almacena su indice en lista (por si son varias)
notaHigher = 0
indicesNotaHigher = []

for i in range(0,cantNotas):
    if (notaHigher <= listaNotas[i]):
        notaHigher = listaNotas[i]

for i in range(0,len(listaNotas)):
    if (notaHigher == listaNotas[i]):
        indicesNotaHigher.append(i)
        
#printea la nota más alta y los indices + 1 (en que posicion la puso)

print("La nota más alta es un ", notaHigher)
print("Osea la/s nota/s en la posicion: ",end="")

for i in indicesNotaHigher:
    print(i + 1, end=" ")

