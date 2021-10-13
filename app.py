from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')



@app.route('/cartelera')
def cartelera():
    return render_template('cartelera.html')



@app.route('/funciones')
def funciones():
    return render_template('funciones.html')


@app.route('/peliculas/venom-carnage-liberado')
def venom():
    return render_template('venom.html')


@app.route('/peliculas/sin-tiempo-para-morir')
def SinTiempo():
    return render_template('007.html')


@app.route('/peliculas/los-locos-addams-2')
def addams():
    return render_template('addams.html')


@app.route('/peliculas/la-leyenda-de-la-viuda')
def viuda():
    return render_template('viuda.html')


@app.route('/peliculas/rock-dog-renace-una-estrella')
def rock():
    return render_template('rock.html')


@app.route('/peliculas/peter-rabbit-conejo-en-fuga')
def peter():
    return render_template('peter.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

'''
@app.route('/prueba-user')
def user():
    return render_template('headeruser.html')'''
