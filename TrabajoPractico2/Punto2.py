def esBisiesto (year):
    year = esEntero(year)
    year = esPositivo(year)

    boolAño = False

    if ((year % 4) == 0) and ((year % 100) != 0 or (year % 400) == 0):
        boolAño = True

    return boolAño
    
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
    return (nro)

def esMes (mes):
    while True:
        if (mes >= 1) and (mes <= 12):
            break
        else: 
            mes = input("El mes ingresado no es válido, ingrese uno entre 1 y 12: ")
            mes = esEntero(mes)
            mes = esPositivo(mes)
            continue
    
    return mes

def esDia (dia,mes,anio):
    while True:
        #si es mes con 31 dias
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if (dia > 0) and (dia <= 31):
                break
            else:
                dia = input("El dia es invalido para el mes ingresado: ")
                dia = esEntero(dia)
                dia = esPositivo(dia)
                continue

        #si es mes con 30 dias
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if (dia > 0) and (dia <= 30):
                break
            else:
                dia = input("El dia es invalido para el mes ingresado: ")
                dia = esEntero(dia)
                dia = esPositivo(dia)
                continue

        #si es febrero
        if (mes == 2):
            #si año es bisiesto
            if (esBisiesto(anio) == True):
                if (dia > 0) and (dia <= 29):
                    break
                else:
                    dia = input("El dia es invalido para el mes ingresado: ")
                    dia = esEntero(dia)
                    dia = esPositivo(dia)
                    continue
            
            #si año no es bisiesto
            else:
                if (dia > 0) and (dia <= 28):
                    break
                else:
                    dia = input("El dia es invalido para el mes ingresado: ")
                    dia = esEntero(dia)
                    dia = esPositivo(dia)
                    continue


    return dia

#MAIN

print("Se le pedira una fecha en el formato año/mes/dia, responda con numeros")

#comprueba si el año es valido 
anio = input("Año: ")
anio = esEntero(anio)
anio = esPositivo(anio)
bisiesto = esBisiesto(anio)

#comprueba si el mes es valido
mes = input("Mes: ")
mes = esEntero(mes)
mes = esPositivo(mes)
mes = esMes(mes)

#comprueba si el dia es valido
dia = input("Dia: ")
dia = esEntero(dia)
dia = esPositivo(dia)
dia = esDia(dia,mes,anio)


#prints
print("Su fecha es %i/%i/%i" % (anio,mes,dia))
print("En formato español es día %i, mes %i y año %i" % (dia,mes,anio))

if (bisiesto == True):
    print("Además el año ingresado es bisiesto")
else:
    print("El año que ingreso no es bisiesto")


