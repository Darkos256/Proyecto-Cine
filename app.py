from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('header.html')

@app.route('/login')

def login():
    return render_template('login.html')

@app.route('/register')

def register():
    return render_template('register.html')

@app.route('/cartelera')

def cartelera():
    return render_template('cartelera.html')

@app.route('/funciones')

def funciones():
    return render_template('funciones.html')


@app.route('/pelicula')

def pelicula():
    return render_template('busqueda.html')