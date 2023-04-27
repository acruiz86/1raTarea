from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Mundo feliz!'
@app.route('/nuevo/')
def nuevo_world():
    return 'el mundo es mejor!'
@app.route('/prueba2/')
def prueba2Ejemplo():
    return 'Ya todo cambio'