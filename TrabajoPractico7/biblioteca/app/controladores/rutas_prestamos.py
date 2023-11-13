from flask import Blueprint, request, jsonify
from modelos.prestamos import obtener_lista_prestamos, obtener_prestamo_xid, agregar_prestamo, devolucion_prestamos_xid

#ACLARACIÓN: de cada libro la biblioteca tiene solamente un ejemplar.
#        * Obtener la lista de todos los libros prestados que aún no se han devuelto (`GET`).
#        * Obtener detalles de un prestamo de libro por su ID (`GET`).
#        * Generar un nuevo prestamo (`POST`). Debe recibir los datos en formato JSON.
#        * Registrar la devolución de un prestamo por su ID (`PUT`). Debe recibir los datos en formato JSON.


#creacion de blueprint

prestamos_blueprint = Blueprint("prestamos", __name__)

@prestamos_blueprint.route("/prestamos/", methods=["GET"])
def get_prestamos():
    return jsonify(obtener_lista_prestamos())

@prestamos_blueprint.route("/prestamos/id/<id>", methods=["GET"])
def get_prestamo_xid(id):
    prestamo = obtener_prestamo_xid(id)
    if prestamo:
        return jsonify(prestamo), 200
    else:
        return jsonify({"error":"prestamo no encontrado"}), 404

@prestamos_blueprint.route("/prestamos/", methods=["POST"])
def post_prestamo_nuevo():
    if request.is_json:
        if ("socio_dni" and "libro_id" and "fecha_retiro" and "fecha_devolucion") in request.json:
            nuevo_prestamo = request.get_json()
            agregar_prestamo(nuevo_prestamo["socio_dni"],nuevo_prestamo["libro_id"],nuevo_prestamo["fecha_retiro"],nuevo_prestamo["fecha_devolucion"])
            return jsonify({"listo":"nuevo prestamo registrado"})
        else: 
            return jsonify({"error":"faltan datos"})
    else:
        return jsonify({"error":"formato no aceptado"})
    
@prestamos_blueprint.route("/prestamos/id/<id>", methods=["PUT"])
def put_devolucion_prestamo(id):
    prestamo = devolucion_prestamos_xid(id)
    if prestamo == "Prestamo devuelto correctamente":
        return jsonify({"listo":"prestamo devuelto correctamente"}), 200
    elif prestamo == "Prestamo no encontrado":
        return jsonify({"error":"prestamo no encontrado"}), 404
    else: 
        return jsonify({"error":"no se encontro el archivo"}), 400
    
