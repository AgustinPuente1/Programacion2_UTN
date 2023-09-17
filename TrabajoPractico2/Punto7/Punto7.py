#abre archivo
leerArchivo = "C:/Agustin/UTN/Programacion II/TrabajoPractico2/Punto7/productos.txt"

archivo = open(leerArchivo,"r")

#prints inicio 
print("Hola, acá tenés la lista de productos")
print("Escriba el nombre del producto que desee ver el precio")


#almacena su respectiva variable
codigoProducto = []
nombrePoductos = []
precioProducto = []

#mete los tres datos de la linea, separadas por los ;
for linea in archivo:
    datos = linea.split(";")
    codigoProducto.append(datos[0])
    nombrePoductos.append(datos[1])
    precioProducto.append(datos[2])
    datos.pop()
    datos.pop()
    datos.pop()

#muestra la lista de nombres de los productos 
for i in nombrePoductos:
    print(i)

#pide nombre del producto para mostrar datos
productoPedido = input("Ingrese el nombre de la misma forma que sale en la lista: ")

for k in range(0,len(codigoProducto)):
    if (productoPedido == nombrePoductos[k]):
        print("El codigo de producto es %s, del producto %s, que vale %s" % (codigoProducto[k],nombrePoductos[k],precioProducto[k]))

              

#cierra archivo
archivo.close()



