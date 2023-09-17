oracion = input("Ingrese un texto: ")

cantCaracteres = len(oracion)
cantLetras = 0
cantEspacios = 0

for i in oracion:
    esletra = i.isalpha()
    if (esletra == True):
        cantLetras += 1
    
    if (i == " "):
        cantEspacios += 1

print ("Cantidad de caracteres= ", cantCaracteres)
print ("Cantidad de letras= ", cantLetras)
print ("Cantidad de espacios= ", cantEspacios)
