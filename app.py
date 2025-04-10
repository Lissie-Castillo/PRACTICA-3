from flask import Flask,render_template 
app = Flask(__name__)

@app.route("/")

def index():
    return "Hola"

@app.route("/Saludo/<string:nombre>/<int:edad>")


def saludar(nombre,edad):
    return "Bienvenido "+nombre+" , yo sé que tú tienes"+ str(edad)

@app.route("/prueba")


def render():
    return render_template("prueba.html")

