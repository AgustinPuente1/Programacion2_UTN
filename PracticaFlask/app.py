from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) #creamos una instancia de la clase Flask

@app.route("/signup/", methods=["GET"])
def show_signup_form_get():
    return "No estas logeado. Esto es un get"
@app.route("/signup/", methods=[ "POST"])
def show_signup_form():
    if request.method == 'POST':
        if 'name' in request.form:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            return "Hola " + name + " " + email + " " + password
    return "No estas logeado. Esto es un POST"
@app.route('/')
def index():
    return '<h1>Hola!</h1>'
