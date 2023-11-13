from flask import Blueprint, jsonify, request
from modelos.libros import obtener_lista_libros, obtener_libro_xid, agregar_libro, actualizar_libro_xid

#creacion de blueprint

libros_blueprint = Blueprint("libros", __name__)

@libros_blueprint.route("/libros/", methods=["GET"])
def get_libros(): 
    return jsonify(obtener_lista_libros())

@libros_blueprint.route("/libros/id/<id>", methods=["GET"])
def get_libro_xid(id):
    libro = obtener_libro_xid(id)
    if libro:
        return jsonify(libro), 200
    else:
        return jsonify({"error":"libro no encontrado"}), 404
    
@libros_blueprint.route("/libros/", methods=["POST"])
def post_libro_nuevo():
    if request.is_json:
        if ("titulo" and "autor" and "anio_publicacion") in request.json:
            nuevo_libro = request.get_json()
            agregar_libro(nuevo_libro["titulo"],nuevo_libro["autor"],nuevo_libro["anio_publicacion"])
            return jsonify({"listo":"nuevo libro agregado"}), 200
        else: 
            return jsonify({"error":"faltan datos"}); 400
    else: 
        return jsonify({"error","formato no aceptado"}), 400

@libros_blueprint.route("/libros/id/<id>", methods=["PUT"])
def put_actualizar_libro(id):      
    if request.is_json:
        if ("titulo" in request.json) or ("autor" in request.json) or ("anio_publicacion" in request.json):
            libro_editar = request.get_json()
            try: 
                titulo_libro = {}
                titulo_libro["titulo"] = libro_editar["titulo"]
            except KeyError:
                titulo_libro = None

            try: 
                autor_libro = {}
                autor_libro["autor"] = libro_editar["autor"]
            except KeyError:
                autor_libro = None

            try: 
                anio_libro = {}
                anio_libro["anio_publicacion"] = libro_editar["anio_publicacion"]
            except KeyError:
                anio_libro = None

            actualizar_libro_xid(id,titulo_libro["titulo"],autor_libro["autor"],anio_libro["anio_publicacion"])
            return jsonify({"listo":"libro actualizado"}), 200
        else:
            return jsonify({"error":"datos erroneos"}), 400
    else: 
        return jsonify({"error":"formato no aceptado"}), 400

          