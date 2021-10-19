import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import get_db
from flask import flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    return render_template('usuario.html')


@app.route('/inicioUser', methods=['GET', 'POST'])
def inicioUser():
    return render_template('index.html')

@app.route( '/login', methods=('GET', 'POST') )
def login():
    try:
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['email']
            password = request.form['password']

            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render_template( 'login.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'login.html' )

            user = db.execute(
                'SELECT * FROM usuarios WHERE email = ? AND contrasena = ? ', (username, password)
            ).fetchone()      

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                return redirect( '/' )
            flash( error )
        return render_template( 'login.html' )
    except:
        return render_template( 'login.html' )





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


@app.route( '/registro_usuarioPaginaUsuario', methods=('GET', 'POST') )
def registro_usuarioPaginaUsuario():
        if request.method == 'POST':
            nombre= request.form['nombre']
            apellido= request.form['apellido']
            correo = request.form['email1']
            correo2 = request.form['email2']
            password = request.form['password']
            name = nombre + apellido

            if(correo == correo2 and len(password)  > 6 and len(password)  < 12):
                db = get_db()
                db.execute(
                    "INSERT INTO usuarios (nombre_usuario, email, contrasena, user,administrador) VALUES ('%s','%s','%s','SI','NO')" % (name, correo, password)
                )

                db.commit()
                #alert
                success_message = 'Usuario Registrado con el nombre de: '+ name +' correo: ' + correo +' fue registrado con exito. '
                flash(success_message)
                #fin alert
                return render_template( 'login.html' )
        return render_template( 'register.html' )

@app.route( '/registro_usuario', methods=('GET', 'POST') )
def registro_usuario():
        if request.method == 'POST':
            name= request.form['nombreCreacion']
            correo = request.form['correoCreacion']
            password = request.form['contrasena1Creacion']
            db = get_db()
            db.execute(
                "INSERT INTO usuarios (nombre_usuario, email, contrasena, user,administrador) VALUES ('%s','%s','%s','SI','NO')" % (name, correo, password)
            )

            db.commit()
            #alert
            success_message = 'Usuario Registrado con el nombre de: '+ name +' correo: ' + correo +' fue registrado con exito. '
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )
# 

@app.route( '/actualizar_usuario', methods=('GET', 'POST') )
def actualizar_usuario():
        if request.method == 'POST':
            correo= request.form['correoActualizar']
            nombre = request.form['nombreActualizar']
            password = request.form['contrasenaActualizar']
            db = get_db()
            db.execute(
                "UPDATE usuarios SET nombre_usuario = '%s' ,contrasena = '%s' WHERE email ='%s'" % (nombre ,password , correo)
            )
            db.commit()
            #alert
            success_message = 'Usuario con correo: ' + correo + ' fue actualizado con exito'
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )

@app.route( '/eliminar_usuario', methods=('GET', 'POST') )
def eliminar_usuario():
        if request.method == 'POST':
            correo = request.form['correoEliminacion']
            db = get_db()
            db.execute(
                "DELETE FROM usuarios WHERE email ='%s'" % correo
            )
            db.commit()
            #alert
            success_message = 'Usuario con correo: '+ correo +' fue eliminado con exito'
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )


@app.route( '/registro_pelicula', methods=('GET', 'POST') )
def registro_pelicula():
        if request.method == 'POST':
            nombrePelicula= request.form['nombrePelicula']
            funcion1 = request.form['funcion1']
            funcion2 = request.form['funcion2']
            funcion3 = request.form['funcion3']
            costo2d = request.form['costo2d']
            costo3d = request.form['costo3d']
            caratula = request.form['caratula']
            descripcion = request.form['descripcion']
            msg = "msg"

            db = get_db()
            db.execute(
                "INSERT INTO peliculas (nombre_pelicula, funcion_uno, funcion_dos, funcion_tres, costo2d, costo3d, caratula, descripcion) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (nombrePelicula, funcion1, funcion2, funcion3, costo2d, costo3d, caratula, descripcion)
            )

            db.commit()
            #alert
            success_message = 'La pelicula '+ nombrePelicula +' fue registrada con exito.'
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )



@app.route( '/actualizar_pelicula', methods=('GET', 'POST') )
def actualizar_pelicula():
        if request.method == 'POST':
            nombrePelicula= request.form['editarNombrePelicula']
            funcion1 = request.form['editarFuncion1']
            funcion2 = request.form['editarFuncion2']
            funcion3 = request.form['editarFuncion3']
            costoFuncion2d = request.form['editarCostoFuncion2d']
            costoFuncion3d = request.form['editarCostoFuncion3d']
            caratula = request.form['editarCaratula']
            descripcion = request.form['editarDescripcion']
            db = get_db()
            db.execute(
                "UPDATE peliculas SET funcion_uno = '%s' ,funcion_dos = '%s' ,funcion_tres = '%s' ,costo2d = '%s' ,costo3d = '%s' ,caratula = '%s' ,descripcion = '%s'  WHERE nombre_pelicula ='%s'" % (funcion1 ,funcion2 ,funcion3 ,costoFuncion2d ,costoFuncion3d ,caratula ,descripcion , nombrePelicula  )
            )
            db.commit()
            #alert
            success_message = 'La pelicula '+ nombrePelicula +' fue actualizada con exito.'
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )


@app.route( '/eliminar_pelicula', methods=('GET', 'POST') )
def eliminar_pelicula():
        if request.method == 'POST':
            pelicula = request.form['eliminar_pelicula']
            db = get_db()
            db.execute(
                "DELETE FROM peliculas WHERE nombre_pelicula ='%s'" % pelicula
            )
            db.commit()
            #alert
            success_message = 'La pelicula '+ pelicula +' fue eliminada con exito.'
            flash(success_message)
            #fin alert
            return render_template( 'admin.html' )
        return render_template( 'admin.html' )