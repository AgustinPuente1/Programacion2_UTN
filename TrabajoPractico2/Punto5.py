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
        if (nro >= 0) and (nro <= 100):
            break
        else:
            nro = input("El numero es mayor a 100 o negativo, escribi otro: ",)
            esEntero(int(nro))
    return nro

#MAIN

print("Ingrese el apellido, nombre y nota (nro entero) del alumno para ser mostrada en pantalla")
print("Cuando quiera salir presione 0 en el nombre o apellido")

#entrada de datos y guardado en listas

listaApellidosYNombre = []
listaNotas = []

while True:
    auxApellidoYNombre = input("Apellido y Nombre: ")
    if (auxApellidoYNombre == "0"):
        break

    auxNota = input("Nota: ")
    auxNota = esEntero(auxNota)
    auxNota = esPositivo(auxNota)

    listaApellidosYNombre.append(auxApellidoYNombre)
    listaNotas.append(auxNota)


#printeado en pantalla  
#10 espacios

print("ALUMNOS","          ","PARCIAL","          ","RESULTADO")

for i in range(0,len(listaApellidosYNombre)):
    
    if (listaNotas[i] >= 40):
        resultado = "Aprobado"
    else: 
        resultado = "Desaprobado"


    print("{:<20}".format(listaApellidosYNombre[i]), "{:<16}".format(listaNotas[i]),resultado)