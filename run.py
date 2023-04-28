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
<<<<<<< HEAD
=======
    a=6
    b=7
    c=a*5+b*8
    print(c)
>>>>>>> features/conteiner
    return 'contenido del sitio !'
