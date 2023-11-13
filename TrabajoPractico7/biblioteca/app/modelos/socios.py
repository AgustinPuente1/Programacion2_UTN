import csv
import os

#socios.py

socios = []

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv_socios = os.path.join(directorio_actual, 'socios.csv')


def obtener_lista_socios(): #devuelve la lista de socios
    if verificador_ruta() == True:
        importar_socios_csv()
        return socios
    else:
        return "No se encontro el archivo"

def obtener_socio_xid(id): #devuelve el socio pedido por id
    if verificador_ruta() == True:
        importar_socios_csv()
        for socio in socios:
            if int(id) == int(socio["id"]):
                return socio
    else:
        return "No se encontro el archivo"

def agregar_socio(nuevo_dni,nuevo_nombre,nuevo_apellido,nuevo_telefono,nuevo_email): #agrega un nuevo socio a la lista de socios
    if verificador_ruta() == True:
        importar_socios_csv()
        nueva_id = 1
        for socio in socios:
            if nueva_id != int(socio["id"]):
                break
            else: 
                nueva_id += 1
        socios.append({
                    "id":nueva_id,
                    "dni":nuevo_dni,
                    "nombre":nuevo_nombre,
                    "apellido":nuevo_apellido,
                    "telefono":nuevo_telefono,
                    "email":nuevo_email
                })
        
        exportar_socios_csv()
        return "Nueva entrada de socio agregada "
        
    else: 
        return "No se encontro el archivo"

def actualizar_socio_xid(id_socio,nuevo_dni=None,nuevo_nombre=None,nuevo_apellido=None,nuevo_telefono=None,nuevo_email=None): #actualiza la lista socios
    if verificador_ruta() == True:
        importar_socios_csv()
        for socio in socios:
            #si la id coincide se fija que datos actualizar y que datos no 
            if int(socio["id"]) == int(id_socio):
                if not nuevo_dni == None:
                    socio["dni"] = nuevo_dni
                if not nuevo_nombre == None:
                    socio["nombre"] = nuevo_nombre
                if not nuevo_apellido == None:
                    socio["apellido"] = nuevo_apellido
                if not nuevo_telefono == None:
                    socio["telefono"] = nuevo_telefono
                if not nuevo_email == None:
                    socio["email"] = nuevo_email
                exportar_socios_csv()
                return "Socio actualizado correctamente"
            
    else: 
        return "No se encontro el archivo"
                
def importar_socios_csv(): #trae el archivo a una lista de diccionarios
    if verificador_ruta() == True:
        with open(ruta_csv_socios, newline='', encoding='utf-8') as csvSocios:
            leer_archivo = csv.DictReader(csvSocios)
            socios.clear()
            for linea in leer_archivo:
                socios.append(linea)
                
    else: 
        socios.append({
            "id":1,
            "dni":12345678,
            "nombre":"Nombre default",
            "apellido":"Apellido default",
            "telefono":2912323123,
            "email":"default@example.com"
        })
    
def exportar_socios_csv(): #actualiza el archivo socios.csv
    if verificador_ruta() == True:
        #abre el archivo con "w" para sobreescribirlo
        with open(ruta_csv_socios,"w",newline='', encoding='utf-8') as csvSocios:
            header = ["id", "dni", "nombre","apellido","telefono","email"]
            writer = csv.DictWriter(csvSocios, fieldnames=header)
            
            if csvSocios.tell() == 0:
                writer.writeheader()

            for socio in socios:
               writer.writerow(socio)
        return "Se exporto correctamente"
    else:
        return "No se encontro el archivo para exportar"
    
def verificador_ruta(): #verifica si la ruta es correcta
    if os.path.exists(ruta_csv_socios):
        return True
    else:
        return False

def borrar_socio_xid(id): #borra al socio con la id
    if verificador_ruta() == True:
        importar_socios_csv()
        i = 0   #para ver en que posicion esta el socio y borrarlo

        for socio in socios:
            if int(id) == int(socio["id"]):
                socios.pop(i)
                exportar_socios_csv()
                return "Socio borrado correctamente"
            else:
                i += 1
        return "Socio no encontrado"
    else: 
        return "No se encontro el archivo"
    
