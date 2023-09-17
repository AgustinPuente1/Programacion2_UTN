def esEntero (nro):
    while True:
        try:
            entero = int(nro)
        except ValueError:
            nro = input("No valido, ingrese otro numero: ",)
            continue
        break
    return nro

#variables

total = 0
cantNros = 0

#prints

print("Ingrese todos los numeros enteros positivos que quieras")
print("Cuando quieras parar pone un numero negativo")
print("Te dara el promedio y la cantidad de ingresos de nros")

#inicio

while True:
    nro = input("Numero: ",)
    nro = esEntero(nro)
    nro = int(nro)

    if (nro < 0):
        break

    total = total + nro
    cantNros += 1

totalPromedio = total/cantNros

print("El promedio es %i con un total de %i ingresos" % (totalPromedio,cantNros))