from flask import Blueprint, request, jsonify
from modelos.socios import actualizar_socio_xid, obtener_lista_socios, obtener_socio_xid,agregar_socio, borrar_socio_xid

#creacion de blueprint

socios_blueprint = Blueprint("socios", __name__)

@socios_blueprint.route("/socios/", methods=["GET"])
def get_socios(): 
    return jsonify(obtener_lista_socios())

@socios_blueprint.route("/socios/id/<id>", methods=["GET"])
def get_socio_xid(id):
    socio = obtener_socio_xid(id)
    if socio:
        return jsonify(socio), 200
    else:
        return jsonify({"error":"socio no encontrado"}), 404
    
@socios_blueprint.route("/socios/", methods=["POST"])
def post_socio_nuevo():
    if request.is_json:
        if ("dni" and "nombre" and "apellido" and "telefono" and "email") in request.json:
            nuevo_socio = request.get_json()
            agregar_socio(nuevo_socio["dni"],nuevo_socio["nombre"],nuevo_socio["apellido"],nuevo_socio["telefono"],nuevo_socio["email"])
            return jsonify({"listo":"nuevo socio agregado"}), 200
        else: 
            return jsonify({"error":"faltan datos"}); 400
    else: 
        return jsonify({"error","formato no aceptado"}), 400
    
@socios_blueprint.route("/socios/id/<id>", methods=["PUT"])
def put_actualizar_socio(id):      
    if request.is_json:
        if ("dni" in request.json) or ("nombre" in request.json) or ("apellido" in request.json) or ("telefono" in request.json) or ("email" in request.json):
            socio_editar = request.get_json()
            try:
                socio_editar = request.json
                dni_socio = socio_editar.get("dni")
                nombre_socio = socio_editar.get("nombre")
                apellido_socio = socio_editar.get("apellido")
                telefono_socio = socio_editar.get("telefono")
                email_socio = socio_editar.get("email")

                actualizar_socio_xid(id, dni_socio, nombre_socio, apellido_socio, telefono_socio, email_socio)

                return jsonify({"listo": "socio actualizado"}), 200
            except:
                return jsonify({"error": "datos erroneos"}), 400
    else: 
        return jsonify({"error":"formato no aceptado"}), 400
    
@socios_blueprint.route("/socios/id/<id>", methods=["DELETE"])
def delete_socio(id):
    socio = borrar_socio_xid(id)
    if socio == "Socio borrado correctamente":
        return jsonify({"listo":"socio borrado"}), 200
    elif socio == "Socio no encontrado":
        return jsonify({"error":"socio no encontrado"}), 404
    else: 
        return jsonify({"error":"no se encontro el archivo"}), 400
    