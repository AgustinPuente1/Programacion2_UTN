leer = "C:/Agustin/UTN/Programacion II/TrabajoPractico2/Punto8/stock.txt"

archivoStock = open(leer,"r")

codigoProducto = []
nombreProducto = []
stockMinimo = []
stockActual = []

for linea in archivoStock:
    datos = linea.split(";")
    datos[2] = int(datos[2])
    datos[3] = int(datos[3])

    if (datos[2] > datos[3]):
        codigoProducto.append(datos[0])
        nombreProducto.append(datos[1])
        stockMinimo.append(datos[2])
        stockActual.append(datos[3])
    




archivoStock.close()

archivoCreado = open("C:/Agustin/UTN/Programacion II/TrabajoPractico2/Punto8/compras.txt","w")

for i in range(0,len(codigoProducto)):
    linea = f"{codigoProducto[i]};{nombreProducto[i]};{stockMinimo[i]-stockActual[i]}\n"
    archivoCreado.write(linea)

archivoCreado.close()