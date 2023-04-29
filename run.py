from flask import Flask
app = Flask(__name__)
@app.route('/')
def holaMundo():
    return 'Mundo FELIZ !'
    
@app.route('/header/')
def headerSite():
    variable = "mensaje nuevo para todos"
    return variable


@app.route('/container/')
def containerSite():
    return 'contenido del sitio !'
