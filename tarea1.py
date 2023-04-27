from flask import Flask
app = Flask(__name__)
@app.route('/')
def holaMundo():
    return 'Mundo FELIZ !'
@app.route('/header/')
def headerSite():
    return 'Encabezado de sitio !'
