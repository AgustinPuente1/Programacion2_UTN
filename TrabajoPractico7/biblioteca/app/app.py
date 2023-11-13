from flask import Flask, request, jsonify
from controladores.rutas_libros import libros_blueprint
from controladores.rutas_socios import socios_blueprint
from controladores.rutas_prestamos import prestamos_blueprint

#blueprints son los controladores, donde estan los @route
#modelos es donde estan las funciones con las que se ejecuta la API

app = Flask(__name__)

app.register_blueprint(libros_blueprint)
app.register_blueprint(socios_blueprint)
app.register_blueprint(prestamos_blueprint)

if (__name__ == "__main__"):
    app.run(debug=True, port=5000)