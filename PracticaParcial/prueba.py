def crearStock(archivo):
    datos = open(archivo,"r")
    datosSeparados = []
    for linea in datos:
        datosSeparados.append(linea.split(", "))

  
    lista = []
    indice = 1
    diccionarioAux = {}
    for i in datosSeparados:
        if (indice == 1):
            diccionarioAux["Nombre"] = str(i[0])
            indice = 2

        if (indice == 2):
            diccionarioAux["Precio"] = float(i[1])
            indice = 3

        if (indice == 3):
     
            diccionarioAux["Cantidad"] = int(i[2])
            lista.append(diccionarioAux)
            diccionarioAux = {}
            indice = 1

   
    return lista

def productoMasCaro(lista):
    mayorPrecio = 0
    nombreMayorProducto = ""
    for i in lista:
        if mayorPrecio < i["Precio"]:
            mayorPrecio = i["Precio"]
            nombreMayorProducto = i["Nombre"]

    return nombreMayorProducto

def productoMenorCantidad(lista):
    prodMenosCant = 9999
    nombreProductoMenorCant = ""
    for i in lista:
        if prodMenosCant > i["Cantidad"]:
            prodMenosCant = i["Cantidad"]
            nombreProductoMenorCant = i["Nombre"]

    return nombreProductoMenorCant

#yo creo que no se puede hacer con reduce porque no me deja en funcion del lambda moverme por los diccionarios
#pongo        reduce(lambda i["Cantidad"], i["Precio"])     y no deja entrar al diccionario
from functools import reduce

def totalGanancia(lista):
    totalPosibleGanancia = 0
    for i in lista:
        gananciaIndividualproducto = i["Cantidad"] * i["Precio"]
        totalPosibleGanancia += gananciaIndividualproducto

    return totalPosibleGanancia

lista = (crearStock("datos.csv")) 

print(productoMasCaro(lista))

print(productoMenorCantidad(lista))

print(totalGanancia(lista))