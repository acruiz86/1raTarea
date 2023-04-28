from flask import Flask
app = Flask(__name__)
@app.route('/')
def holaMundo():
    return 'Mundo FELIZ !'
    
@app.route('/header/')
def headerSite():
    a=8
    b=50
    c=a*b/5 
    return 'Encabezado de sitio !'


@app.route('/container/')
def containerSite():
    return 'contenido del sitio !'