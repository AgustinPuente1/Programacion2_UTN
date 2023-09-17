texto = input("Ingresa un texto y te va a dar la cantidad de vocales: ",)
texto = str(texto)

cantVocales = 0

for i in texto:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        cantVocales += 1
    if (i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        cantVocales += 1

print ("La cantidad de vocales en el texto escrito son %i " % (cantVocales))