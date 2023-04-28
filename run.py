from flask import Flask
app = Flask(__name__)
@app.route('/')
def holaMundo():
    return 'Mundo FELIZ !'

@app.route('/header/')
def headerSite():
    return 'Encabezado de sitio !'

@app.route('/container/')
def containerSite():
    a = 8
    b = 9
    c = a * b
    return 'contenido del sitio !'