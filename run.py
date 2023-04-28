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
    a=0
    if a>0:
        a=0
    else:
        a=60
    return 'contenido del sitio !'