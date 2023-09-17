def esEntero (nro):
    while True:
        try:
            entero = int(nro)
        except ValueError:
            nro = input("No valido, ingrese otro numero: ",)
            continue
        break
    return nro

#inicio            

print("Escribi todos los numeros que quieras...")
print("Cuando querias terminar pone basta")
print("Te va a dar la suma de todas y el promedio de los valores")

total = 0
cantNros = 0

while True:
    nro = input("Numero: ",)

    if (nro == "basta"):
        break

    nro = esEntero(nro)
    nro = float(nro)

    total = total + nro
    cantNros += 1



print ("Los numeros puestos son: ",cantNros)
print ("La suma de todos los numeros son: ",total)

totalPromedio = total/cantNros

print ("El promedio de los numeros es: ",totalPromedio)




