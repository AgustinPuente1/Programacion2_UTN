from flask import Flask, request, url_for, render_template, jsonify

app = Flask(__name__)

destinos_argentina = [
    {
        "id": 1,
        "ciudad": "Buenos Aires",
        "fecha_ida": "2023-06-15",
        "fecha_vuelta": "2023-06-20",
        "descripcion": "La capital de Argentina es una ciudad vibrante con una rica historia y una escena cultural diversa.",
        "tipo_viaje": "turismo",
        "precio": 40000,
        "estrellas": 5,
        "pension": "all inclusive",
        "transporte": "avión",
        "cupo_max": 20,
        "cupo_actual": 20
    },
    {
        "id": 2,
        "ciudad": "Bariloche",
        "fecha_ida": "2023-07-10",
        "fecha_vuelta": "2023-07-17",
        "descripcion": "Bariloche es famosa por sus paisajes montañosos, los productos regionales y sus chocolates artesanales.",
        "tipo_viaje": "turismo",
        "precio": 35000,
        "estrellas": 4,
        "transporte": "avión",
        "cupo_max": 30,
        "cupo_actual": 30
    },
    {
        "id": 3,
        "ciudad": "Mendoza",
        "fecha_ida": "2023-08-05",
        "fecha_vuelta": "2023-08-12",
        "descripcion": "Mendoza es el centro del vino argentino y ofrece hermosos paisajes de viñedos y montañas.",
        "tipo_viaje": "turismo",
        "precio": 30000,
        "estrellas": 3,
        "transporte": "avión",
        "cupo_max": 20,
        "cupo_actual": 20
    },
    {
        "id": 4,
        "ciudad": "Salta",
        "fecha_ida": "2023-09-20",
        "fecha_vuelta": "2023-09-25",
        "descripcion": "Salta es conocida por su arquitectura colonial, montañas coloridas y folklore.",
        "tipo_viaje": "educativo",
        "precio": 20000,
        "estrellas": 4,
        "transporte": "colectivo",
        "cupo_max": 50,
        "cupo_actual": 50
    },
    {
        "id": 5,
        "ciudad": "Córdoba",
        "fecha_ida": "2023-10-15",
        "fecha_vuelta": "2023-10-20",
        "descripcion": "Córdoba es famosa por sus sierras y su cultura universitaria.",
        "tipo_viaje": "educativo",
        "precio": 15000,
        "estrellas": 2,
        "transporte": "colectivo",
        "cupo_max": 40,
        "cupo_actual": 40
    }
]

# MUESTRA TODOS LOS VIAJES

@app.route('/viajes/', methods=["GET"])
def obtener_viajes():
    print("SE EJECUTO UN GET REQUEST PARA OBTENER TODO LOS VIAJES")
    print("EJECUTADO CORRECTAMENTE")
    return jsonify(destinos_argentina)

# MUESTRA UN VIAJE DE TODOS

@app.route('/viajes/id/<id>', methods=["GET"])
def obtener_viajes_porID(id):
    for viaje in destinos_argentina:
        if viaje["id"] == int(id):
            viaje_specs = viaje
            print("SE EJECUTO UN GET REQUEST PARA OBTENER UN VIAJE CON ID ",id)
            print("EJECUTADO CORRECTAMENTE")
            return jsonify(viaje_specs)

    print("SE EJECUTO UN GET REQUEST PARA OBTENER UN VIAJE CON ID ",id)
    print("LA ID NO EXISTE")
    return "No se encuentro un viaje con esa ID"

# AGREGA UN VIAJE CON UNA ID BUSCADA

@app.route('/viajes/', methods=["POST"])
def agregar_viaje():
    nueva_id = 1
    for viajes_id in destinos_argentina: 
        if int(viajes_id["id"]) == nueva_id:
            nueva_id += 1
        else:
            exit
    nuevo_viaje = request.form.to_dict()
    nuevo_viaje["id"] = nueva_id
    destinos_argentina.append(nuevo_viaje)

    print("SE EJECUTO UN POST REQUEST PARA AGREGAR UN VIAJE")
    print(request.form)
    print("EJECUTADO CORRECTAMENTE")
    return "Se agrego correctamente"

# ACTUALIZA UN VIAJE POR ID

@app.route('/viajes/id/<id>', methods=["PUT"])
def actualizar_viaje(id):
    actualizacion_viaje = request.json
    
    print(actualizacion_viaje)
    
    for viaje in destinos_argentina:
        if (int(viaje["id"]) == int(id)):
            viaje.update(actualizacion_viaje)
            print("SE EJECUTO UN PUT REQUEST PARA MODIFICAR UN VIAJE")
            print("EJECUTADO CORRECTAMENTE")
            return "Se modifico correctamente"
    
    print("SE EJECUTO UN PUT REQUEST PARA MODIFICAR UN VIAJE CON ID ",id)
    print("NO SE ENCONTRO UN VIAJE CON ESA ID")
    return "No se encuentro un viaje con esa ID"

# BORRA UN VIAJE POR ID

@app.route('/viajes/id/<id>', methods=["DELETE"])
def borrar_viaje(id):
    cont_borrador = 0
    for viaje in destinos_argentina:
        if (int(viaje["id"]) == int(id)):
            destinos_argentina.pop(cont_borrador)
            print("SE EJECUTO UN DELETE REQUEST PARA BORRAR UN VIAJE CON ID ",id)
            print("SE BORRO CORRECTAMENTE")
            return "Se borro correctamente"
        cont_borrador += 1
    
    print("SE EJECUTO UN DELETE REQUEST PARA BORRAR UN VIAJE CON ID ",id)
    print("NO SE ENCONTRO UN VIAJE CON ESA ID")
    return "No se encontro un viaje con esa ID"



app.run(debug=True, port=5000)