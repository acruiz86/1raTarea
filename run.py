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
    a = 8
    b = 9
    c = a * b
    return 'contenido del sitio !'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8085")
