print ("Escribi un texto para calcular la cantidad de espacios:")
texto = input("")
cantEspacios = 0

for i in texto: 
    if (i == " "):
        cantEspacios += 1

print (cantEspacios)