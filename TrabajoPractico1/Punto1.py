def esEntero (nro):
    while True:
        try:
            entero = int(nro)
        except ValueError:
            nro = input("No valido, ingrese otro numero: ",)
            continue
        break
    return nro

def esPositivo (nro):
    while True: 
        nro = int(nro)
        if (nro > 0):
            print("Tu nro es positivo y entero")
            break
        else:
            nro = input("El numero es 0 o negativo, escribi otro: ",)
            esEntero(int(nro))
    return (nro)

#INICIO
#hola

print("Calculadora de tipos de triangulos...")

lado1 = input("Primer lado: ",)
lado1 = esEntero(lado1)
lado1 = esPositivo(lado1)            
    
lado2 = input("Segundo lado: ",)
lado2 = esEntero(lado2)
lado2 = esPositivo(lado2)

lado3 = input("Tercer lado: ",)
lado3 = esEntero(lado3)
lado3 = esPositivo(lado3)

#Equilatero 

if(lado1 == lado2) and (lado1 == lado3):
    print ("Triangulo equilatero")

#Isoseles

if(lado1 == lado2) and (lado1 != lado3):
    print ("Triangulo isoseles")
if(lado1 != lado2) and (lado1 == lado3):
    print ("Triangulo isoseles")
if(lado2 == lado3) and (lado1 != lado2):
    print ("Triangulo isoseles")     

#Escaleno

if(lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
    print ("Triangulo escaleno")
