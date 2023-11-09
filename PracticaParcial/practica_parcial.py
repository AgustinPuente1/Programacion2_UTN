# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='27-03-2003'  
minombre='Agustín Puente'
milegajo=21286
midni=44881251
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.
# ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2

def hashFecha(stringfecha):
    #separa el string en los 3 nros y los vuelve int para sumarlos 
    listaNros = stringfecha.split("-")
    listaNros = [int(nro) for nro in listaNros]
    restoDe4 = (listaNros[0]+listaNros[1]+listaNros[2]) % 4
    return restoDe4

# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.    
# Funcionamiento: Teniendo una lista se van comparando dos numeros y "sube" al que es más grande, terminando con el orden de todos los numero
# Algoritmo: El algoritmo funciona de la siguente manera, en una lista de n numeros, se utilizan dos "for" para orden la lista.
# El primer for se utiliza para dar las vueltas a la lista y el segundo es el que se encarga de comparar los numeros adyacentes,
# luego verifica si el primero es más grande que el segundo, si esto es correcto el primer nro pasa a la posición del segundo nro y
# el segundo nro a la posición del primer nro, de esta forma compara los numeros de toda la lista (primero el 0 1, luego 1 2,2 3, y asi hasta el final).
# De esta forma en esta primera vuelta el nro que siempre queda en su orden es el ultimo, por lo que la siguente vuelta no pasara por esa posicion, cada vuelta compara un nro menos.
# Luego da otra vuelta haciendo lo mismo, si la lista tiene n numeros, esto se repite n - 1 veces.
# De esta forma cada numeros va subiendo segun lo grande que sea y termina ordenalo. 



# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(archivo):
    #abro el archivo, por cada linea le separo los datos y lo meto a una lista de datos separados
    datos = open(archivo,"r")
    datosSeparados = []
    for linea in datos:
        datosSeparados.append(linea.split(", "))

    #meto los datos en una lista compuesta por diccionarios de 3 keys
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

#4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
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

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)

#yo creo que no se puede hacer con reduce porque no me deja en funcion del lambda moverme por los diccionarios
#pongo        reduce(lambda i["Cantidad"], i["Precio"])     y no deja entrar al diccionario
from functools import reduce

def totalGanancia(lista):
    totalPosibleGanancia = 0
    for i in lista:
        gananciaIndividualproducto = i["Cantidad"] * i["Precio"]
        totalPosibleGanancia += gananciaIndividualproducto

    return totalPosibleGanancia
