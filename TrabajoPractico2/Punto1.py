#cadena 
cadena = input("Ingrese una cadena para ser analizada: ")

cadenaAlReves = str()

for i in reversed(cadena):
    cadenaAlReves = cadenaAlReves + i

print("Cadena ingresa: ",cadena)
print("Cadena ingresa a la inversa: ",cadenaAlReves)


if (cadena == cadenaAlReves):
    print("Tu cadena es un palindromo, osea se escribe igual al reves")
else:
    print("Tu palabra no es un palindromo")