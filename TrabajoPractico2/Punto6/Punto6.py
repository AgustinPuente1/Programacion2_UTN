#preparado para leer el archivo

leer = "c:/Agustin/UTN/Programacion II/TrabajoPractico2/Punto6/distancia.txt"

archivo = open(leer,"r")

#metiendo las velocidades de cada linea del archivo a una lista

listaVelocidades = []

for i in archivo:
    i = int(i)
    listaVelocidades.append(i)

#sumando todas las velocidades y sacando el promedio

totalVelocidadaes = 0
for i in listaVelocidades:
    totalVelocidadaes = totalVelocidadaes + i

promedioVelocidades = totalVelocidadaes / len(listaVelocidades)

#printeo

print("El promedio de la velocidades en el archivo son: ",promedioVelocidades)

#cierra archivo

archivo.close()