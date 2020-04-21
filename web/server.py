from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/esprimo/<numero>')
def esprimo(numero):
    if (int(numero) > 1):
        for i in range(2, int(numero)):
            if (int(numero) % i) == 0:
                return str(numero) + " no es un numero primo"
        else:
            return str(numero) + " es primo"
    else:
        return str(numero) + " no es un numero primo"

@app.route('/palindrome/<palabra>')
def palindrome(palabra):
    reverso = palabra[::-1]
    return palabra + " es un palíndrome" if palabra == reverso else palabra + " no es palíndrome" 

@app.route('/multiplo/<numero1>/<numero2>')
def multiplo(numero1, numero2):
    return "son múltiplos" if int(numero1) % int(numero2) == 0 else "no son múltiplos"


@app.route('/static/html/<content>')
def static_content(content):
    return render_template(content)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
