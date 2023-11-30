import requests
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    numero_aleatorio = randint(1,150)
    respuesta = requests.get(f'https://pokeapi.co/api/v2/pokemon/{numero_aleatorio}')
    datos = respuesta.json()
    return render_template('index.html', pokemon = datos)

if __name__ == '__main__':
    app.run()
