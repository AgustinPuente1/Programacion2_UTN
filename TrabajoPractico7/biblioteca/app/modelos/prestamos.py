import csv
import os

#prestamos.py

prestamos = [] #id,socio_dni,libro_id,fecha_retiro,fecha_devolucion

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv_prestamos = os.path.join(directorio_actual, 'prestamos.csv')

#ACLARACIÓN: de cada libro la biblioteca tiene solamente un ejemplar.
#        * Obtener la lista de todos los libros prestados que aún no se han devuelto (`GET`).
#        * Obtener detalles de un prestamo de libro por su ID (`GET`).
#        * Generar un nuevo prestamo (`POST`). Debe recibir los datos en formato JSON.
#        * Registrar la devolución de un prestamo por su ID (`PUT`). Debe recibir los datos en formato JSON.

def obtener_lista_prestamos():
    if verificador_ruta() == True:
        importar_prestamos_csv()
        if not prestamos:
            return {"error":"No hay prestamos registrados"}
        return prestamos
    else:
        return {"error":"No se encontro el archivo"}

def obtener_prestamo_xid(id):
    if verificador_ruta() == True:
        importar_prestamos_csv()
        for prestamo in prestamos:
            if int(id) == int(prestamo["id"]):
                return prestamo
    else:
        return "No se encontro el archivo"

def agregar_prestamo(nuevo_dni,nueva_id_libro,nueva_fecha_retiro,nueva_fecha_devolucion):
    if verificador_ruta() == True:
        importar_prestamos_csv()
        nueva_id = 1
        for prestamo in prestamos:
            if str(prestamo["libro_id"]) == str(nueva_id_libro):
                return "Ese libro ya esta prestado"

        for prestamo in prestamos: #se fija que id puede tomar
            if nueva_id != int(prestamo["id"]):
                break
            else:
                nueva_id += 1
        prestamos.append({
            "id":nueva_id,
            "socio_dni":nuevo_dni,
            "libro_id":nueva_id_libro,
            "fecha_retiro":nueva_fecha_retiro,
            "fecha_devolucion":nueva_fecha_devolucion
        })

        exportar_prestamos_csv()
        return "Nuevo prestamo de libro agregado"
    else:
        return "No se encontro el archivo"

def devolucion_prestamos_xid(id):
    if verificador_ruta() == True:
        importar_prestamos_csv()

        for prestamo in prestamos:
            if int(id) == int(prestamo["id"]):
                prestamos.remove(prestamo)
                exportar_prestamos_csv()
                return "Prestamo devuelto correctamente"
        return "Prestamo no encontrado"
    else: 
        return "No se encontro el archivo"

def importar_prestamos_csv():
    if verificador_ruta() == True:
        with open(ruta_csv_prestamos,newline='', encoding="utf-8") as csvPrestamos:
            leer_archivo = csv.DictReader(csvPrestamos)
            prestamos.clear()
            for linea in leer_archivo:
                prestamos.append(linea)    

            return "Importacion correcta"

    else: 
        return "No hay datos para importar"   

def exportar_prestamos_csv():
    if verificador_ruta() == True:
        with open(ruta_csv_prestamos,"w",newline='', encoding="utf-8") as csvPrestamos:
            header = ["id","socio_dni","libro_id","fecha_retiro","fecha_devolucion"]
            writer = csv.DictWriter(csvPrestamos, fieldnames=header)

            writer.writeheader()            

            for prestamo in prestamos:
                writer.writerow(prestamo)
        
        return "Se exporto correctamente"
    else:
        return "No se encontro el archivo para exportar"

def verificador_ruta():
    if os.path.exists(ruta_csv_prestamos):
        return True
    else:
        return False
    
