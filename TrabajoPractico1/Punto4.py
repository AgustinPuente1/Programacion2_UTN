def esNro (nro):
    while True:
        try:
            posibleNro = float(nro)
            print ("Numero valido...")
        except ValueError:
            print ("No es un Nro...")
            nro = input("Inserte un numero: ",)
            continue
        break
    return nro

def nroMayor (nro1, nro2, nro3):
    nro1 = round(nro1,2)
    nro2 = round(nro2,2)
    nro3 = round(nro3,2)

    if (nro1 >= nro2) and (nro1 >= nro3):
        if (nro1 == nro2) and (nro1 > nro3):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro1,nro2,nro3))
        if (nro1 > nro2) and (nro1 == nro3):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro1,nro3,nro2))
        if (nro1 == nro2) and (nro1 == nro3):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro1,nro2,nro3))  
        if (nro1 > nro2) and (nro1 > nro3):
            if (nro2 > nro3):
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro1,nro2,nro3))
            else: 
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro1,nro3,nro2))

    if (nro2 >= nro1) and (nro2 >= nro3):
        if (nro2 == nro1) and (nro2 > nro3):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro2,nro1,nro3))
        if (nro2 > nro1) and (nro2 == nro3):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro2,nro3,nro1))
        if (nro2 > nro1) and (nro2 > nro3):
            if (nro1 > nro3):
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro2,nro1,nro3))
            else:
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro2,nro3,nro1))
    
    if (nro3 >= nro1) and (nro3 >= nro2):
        if (nro3 == nro1) and (nro3 > nro2):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro3,nro1,nro2))
        if (nro3 > nro1) and (nro3 == nro2):
            print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro3,nro2,nro1))
        if (nro3 > nro1) and (nro3 > nro2):
            if (nro1 > nro2):
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro3,nro1,nro2))
            else:
                print ("1er Nro: %f, 2do Nro: %f, 3er Nro: %f" % (nro3,nro2,nro1))
    

Nro1 = input("Primer nro: ",)
Nro1 = float(esNro(Nro1))

Nro2 = input("Segundo nro: ",)
Nro2= float(esNro(Nro2))

Nro3 = input("Tercer nro: ",)
Nro3 = float(esNro(Nro3))


nroMayor(Nro1,Nro2,Nro3)
