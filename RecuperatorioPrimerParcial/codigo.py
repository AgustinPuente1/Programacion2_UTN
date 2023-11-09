from functools import reduce

nombre = ""
fechaNacimiento = "dd-mm-aaaa"
DNI = ""
legajo = ""

def es_bisiesto (anio):
    if ((anio % 4) == 0) and (((anio % 100) != 0) or (anio % 400 == 0)):
        return True
    else: 
        return False
    
def es_primo(n):
  for i in range(2,n):
    if (n % i) == 0:
      return False
  return True

def hashPrimerParcial (stringNombre,stringFecha):
    #validacion si la fecha es correcta
    try:
        fechaSeparada = stringFecha.split("-")
        dia = int(fechaSeparada[0])
        mes = int(fechaSeparada[1])
        anio = int(fechaSeparada[2])
    except ValueError:
        return False

    if (dia > 31) and ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes ==12)):
        return False
    if (dia >= 31) and ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):
        return False 
    if ((dia > 28) and (mes == 2) and not es_bisiesto(anio)) or ((dia > 29) and (mes == 2) and es_bisiesto(anio)):
        return False
    if (mes > 12) or (mes < 1):
        return False
    if (anio < 1): 
        return False

    #separa las letras y las mete en una lista por su codigo ASCII

    caracteresSeparados = []
    for caracter in stringNombre:
        caracteresSeparados.append(ord(caracter))

    #suma todos los caracteres 

    sumaCaracteres = reduce(lambda x, y: x + y, caracteresSeparados)

    #return

    if (sumaCaracteres % 2) == 1:
        resto = (sumaCaracteres + dia) % 5
        return (resto + anio) % 7
    else: 
        resto = (sumaCaracteres + mes) % 5
        return (resto + anio) % 7

#EJEMPLO: print(hashPrimerParcial("Julian","12-02-2000"))


# 1) implementar una funcion hashPrimerParcial(stringNombre, stringFecha) que recibe un nombre y una fecha de nacimiento y devuelve un numero 
# entero que representa el hash de la persona. stringFecha tiene formato "dd-mm-aaaa". El hash se calculará de la siguiente forma:
# Se deben sumar los valores ASCII de los caracteres del nombre. (los valores ASCII se obtienen con la funcion "ord(caracter)" de python)
# Si la suma de los caracteres es un numero impar se debe sumar el dia de la fecha de nacimiento y calcular el residuo de la division por 5.
# Si la suma de los caracteres es un numero par se debe sumar el mes de la fecha de nacimiento y calcular el residuo de la division por 5.
# Luego, a ese resultado se le suma el año, y se calcula el módulo de la división por 7 (es el valor final que retorna la función).
# Asegúrate de incluir manejo de errores para verificar que la cadena de fecha esté en el formato correcto y que los valores de día, mes y año sean números enteros.

def procesarVentas(rutaArchivo,cantidadEntradas):
    #verificacion
    try:
        datos = open(rutaArchivo,"r")
    except FileNotFoundError:
        print("Error en encontrar el Archivo")
        return False
    
    #separa los datos en listas en la que datosSeparados[i][0] es el nombre y datosSeparados[i][1] la cantidad que quiere comprar
    datosSeparados = []
    for linea in datos:
        datosSeparados.append(linea.split(","))
    
    #prints
    print("Hay %i entradas disponibles se recibieron las siguientes solicitudes:" % (cantidadEntradas))
    for listaNombreEntradas in datosSeparados:
        if (cantidadEntradas > 0) and (((cantidadEntradas - int(listaNombreEntradas[1]))) <= 0):
            print("%s compro %i pero queria comprar %i" % (listaNombreEntradas[0],cantidadEntradas,int(listaNombreEntradas[1])))
            cantidadEntradas = 0
            print("Socios que no pudieron comprar entradas: ")
        if (cantidadEntradas == 0):
            print(listaNombreEntradas[0])   
        if (cantidadEntradas > 0) and ((cantidadEntradas - int(listaNombreEntradas[1])) > 1):
            cantidadEntradas -= int(listaNombreEntradas[1])
            print("%s, %i entradas" % (listaNombreEntradas[0],int(listaNombreEntradas[1])))
            if (cantidadEntradas == 0):
                print("Socios que no pudieron comprar entradas: ")

        
    datos.close()
    return None


rutaArchivo = "RecuperatorioPrimerParcial\entradas.csv"
entradasDisponibles = 20
#procesarVentas(rutaArchivo,entradasDisponibles)















# 5) Dadas dos listas de diccionarios, una con listado de productos y precios, y otra con listado de productos y cantidad de unidades en stock próximas al vencimiento, 
# generar una nueva lista de diccionarios que contenga para cada producto la cantidad de unidades que están por vencer y un precio promocional con 20% de descuento.
# Ejemplo:
# lista_precios = [{"producto": "arroz", "precio": 125.50}, {"producto": "fideos", "precio": 50.75}, {"producto": "pan", "precio": 35.00}]
# lista_stock_a_vencer = [{"producto": "arroz", "cantidad": 100}, {"producto": "fideos", "cantidad": 200}, {"producto": "pan", "cantidad": 300}]
# lista_resultado = [{"producto": "arroz", "cantidad": 100, "precio_promocional": 112.95}, {"producto": "fideos", "cantidad": 200, "precio_promocional": 45.675}, {"producto": "pan", "cantidad": 300, "precio_promocional": 31.5}]


lista_precios = [
    {"producto": "arroz", "precio": 125.50}, {"producto": "fideos", "precio": 50.75},
    {"producto": "pan", "precio": 35.00}, {"producto": "leche", "precio": 80.00}, 
    {"producto": "azucar", "precio": 45.00}, {"producto": "harina", "precio": 55.00},
    {"producto": "aceite", "precio": 100.00}, {"producto": "yerba", "precio": 110.00},
    {"producto": "galletitas", "precio": 70.00}, {"producto": "cacao", "precio": 90.00}
    ]
lista_stock_a_vencer = [
    {"producto": "arroz", "cantidad": 400}, {"producto": "fideos", "cantidad": 200}, 
    {"producto": "pan", "cantidad": 300}, {"producto": "leche", "cantidad": 100},
    {"producto": "galletitas", "cantidad": 50}, {"producto": "cacao", "cantidad": 150}]

def generarLista(lista_precios, lista_stock_a_vencer):
    lista_resultado = []
    #compara si el producto de la lista de precios esta en la lista de stock, y si esta agrega un diccionario con producto,cantidad y precio promocional, a la lista resultado
    for productoListaPrecio in lista_precios:
        for productoListaStock in lista_stock_a_vencer:
            if (productoListaPrecio["producto"] == productoListaStock["producto"]):
                lista_resultado.append({"producto":productoListaPrecio["producto"],"cantidad":productoListaStock["cantidad"],"precio_promocional":productoListaPrecio["precio"] * 0.8})
    return lista_resultado

print(generarLista(lista_precios,lista_stock_a_vencer))