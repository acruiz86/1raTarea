from flask import Flask
app = Flask(__name__)
@app.route('/')
def holaMundo():
    return 'Mundo feliz!'
@app.route('/nuevo/')
def endPoint1():
    return 'el mundo es mejor!'
@app.route('/pruaba4/')
def endPoint2():
    return 'Ya todo cambio'