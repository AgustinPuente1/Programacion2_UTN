#1) 
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

def hashFecha2(stringfecha):
    #intenta separar el string en int de dia/mes/año
    try:
        fechaSeparada = stringfecha.split("-")
        dia = int(fechaSeparada[0])
        mes = int(fechaSeparada[1])
        anio = int(fechaSeparada[2])
    except ValueError:
        return False
    
    #verificacion
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
    
    sumaDiaMes = dia + mes
    if ((anio % 2) == 0):
        anioPar = (sumaDiaMes ** 2) % 5 
        if (es_primo(sumaDiaMes) == True): 
            return (anioPar + anio) % 6  
        else: 
            return (anioPar - anio) & 7
    else:
        anioImpar = (sumaDiaMes ** 3) % 5
        if (es_primo(sumaDiaMes) == True): 
            return (anioImpar + anio) % 6  
        else: 
            return (anioImpar - anio) & 7
        
print(hashFecha2("02-10-2023"))
#2 

#Un pull request es cuando alguien que haya hecho una rama de un repositorio en github mande un solicitud
#para que ese fork que contiene los commits del codigo modificado, sea incorporado al codigo original.
#La solitud debe ser aceptada por los propietorias del codigo original

#3

nombres = ["Alice", "Bob", "Charlie", "david", "Ella", "Frank", "Grace", "harry", "Isabel", "Jack", "Karen", "Liam", "Mia", "Noah", "Olivia", "peter", "Quinn", "Rachel", "Sarah", "Tom", "Ursula", "Victor", "Wendy", "Xander", "Yasmine", "Zane"]
def ordenarNombres(listanombres):
    listanombres = sorted(listanombres, key=str.lower)
    return  listanombres

print(ordenarNombres(nombres))

#4

def procesarVentas(rutaArchivoCSV,cantidadPaquetesDisponibles):
    #verificacion
    try:
        datos = open(rutaArchivoCSV,"r")
    except FileNotFoundError:
        return False
    
    #separa los datos
    datosSeparados = []
    for linea in datos:
        datosSeparados.append(linea.split(","))
    
    #prints
    print("Hay %i paquetes" % (cantidadPaquetesDisponibles))
    for i in datosSeparados:
        if (cantidadPaquetesDisponibles > 0) and (((cantidadPaquetesDisponibles - int(i[1]))) <= 0):
            print("%s quiso comprar %i pero solo quedaban %i" % (i[0],int(i[1]),cantidadPaquetesDisponibles))
            cantidadPaquetesDisponibles = 0
        if (cantidadPaquetesDisponibles == 0):
            print("%s no pudo comprar porque no habia más" % (i[0]))   
        if (cantidadPaquetesDisponibles > 0) and ((cantidadPaquetesDisponibles - int(i[1])) > 1):
            cantidadPaquetesDisponibles -= int(i[1])
            print("%s compro %i" % (i[0],int(i[1])))

        
    datos.close()
    return None

procesarVentas("programacion2\PrimerParcial\compradores.csv",200)

#5 
dicEdades = {"Juan":30,"María":25,"Carlos":35,"Ana":28,"Luis":32,"Laura":29,"Pedro":31,"Sofía":26,"Miguel":27,"Isabel":24,"Diego":33,"Valentina":22,"Javier":29,"Carmen":40,"Andrés":38,"Lucía":27,"Ricardo":36,"Victoria":23,"Gabriel":34,"Fernanda":31,"Max":29,"Diana":28,"Rodrigo":30,"Camila":25,"Gonzalo":33,"Daniela":27,"Emilio":29,"Marcela":34,"José":39,"Valeria":26,"Andrea":30,"Raúl":42,"Sara":24,"Rafael":36,"Elena":25,"Martín":32,"Beatriz":28,"Pablo":37,"Lorena":30,"Ángel":29,"Paula":26,"Luisa":35,"Arturo":31,"Mónica":27,"Manuel":28,"Verónica":29,"Carlos":40}

def invertirDiccionario(diccionario):
    diccionarioinvertido = {}
    for i in diccionario:
        if (diccionario[i] not in diccionarioinvertido):
            diccionarioinvertido[diccionario[i]] = [i]
        else: 
            diccionarioinvertido[diccionario[i]].append(i)
    
#    intente hacerlo todo de una con un list (este caso dict) comprehensions pero no me salio
#    dejo el intento aca por si quieren corregirlo
#    diccionarioinvertido = {edad:[nombre] if edad not in diccionarioinvertido else edad.append(nombre)for nombre, edad in diccionario}
    
    return diccionarioinvertido

    
print(invertirDiccionario(dicEdades))