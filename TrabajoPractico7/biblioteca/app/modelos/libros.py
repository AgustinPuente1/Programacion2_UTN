import csv
import os
from flask import jsonify

#libros.py

libros = []

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv_libros = os.path.join(directorio_actual, 'libros.csv')

def obtener_lista_libros(): #devuelve la lista de libros
    if verificador_ruta() == True:
        importar_libros_csv()
        return libros
    else:
        return "No se encontro el archivo"

def obtener_libro_xid(id): #devuelve el libro pedido por id
    if verificador_ruta() == True:
        importar_libros_csv()
        for libro in libros:
            if int(id) == int(libro["id"]):
                return libro
    else:
        return "No se encontro el archivo"

def agregar_libro(nuevo_titulo,nuevo_autor,nuevo_anio): #agrega un nuevo libro a la lista de libros
    if verificador_ruta() == True:
        importar_libros_csv()
        nueva_id = 1
        for libro in libros:
            if nueva_id != int(libro["id"]):
                break
            else: 
                nueva_id += 1
        libros.append({
                    "id":nueva_id,
                    "titulo":nuevo_titulo,
                    "autor":nuevo_autor,
                    "anio_publicacion":nuevo_anio
                })
        
        exportar_libros_csv()
        return "Nueva entrada de libro agregada, "
        
    else: 
        return "No se encontro el archivo"

def actualizar_libro_xid(id_libro,nuevo_titulo=None,nuevo_autor=None,nuevo_anio=None): #actualiza la lista libros
    if verificador_ruta() == True:
        importar_libros_csv()
        for libro in libros:
            #si la id coincide se fija que datos actualizar y que datos no 
            if int(libro["id"]) == int(id_libro):
                if not nuevo_titulo == None:
                    libro["titulo"] = nuevo_titulo
                if not nuevo_autor == None:
                    libro["autor"] = nuevo_autor
                if not nuevo_anio == None:
                    libro["anio_publicacion"] = nuevo_anio
                exportar_libros_csv()
                return "Usuario actualizado correctamente"
            
    else: 
        return "No se encontro el archivo"
                
def importar_libros_csv(): #trae el archivo a una lista de diccionarios
    if verificador_ruta() == True:
        with open(ruta_csv_libros, newline='') as csvLibros:
            leer_archivo = csv.DictReader(csvLibros)
            libros.clear()
            for linea in leer_archivo:
                libros.append(linea)
                
    else: 
        libros.append({
            "id":1,
            "titulo":"Titulo default",
            "autor":"Autor default",
            "anio_publicacion":1990
        })
    
def exportar_libros_csv(): #actualiza el archivo libros.csv
    if verificador_ruta() == True:
        #abre el archivo con "w" para sobreescribirlo
        with open(ruta_csv_libros,"w",newline='') as csvLibros:
            header = ["id", "titulo", "autor","anio_publicacion"]
            writer = csv.DictWriter(csvLibros, fieldnames=header)
            
            if csvLibros.tell() == 0:
                writer.writeheader()

            for libro in libros:
               writer.writerow(libro)
        return "Se exporto correctamente"
    else:
        return "No se encontro el archivo para exportar"
    
def verificador_ruta(): #verifica si la ruta es correcta
    if os.path.exists(ruta_csv_libros):
        return True
    else:
        return False

