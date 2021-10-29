from datetime import date
from flask import Flask, render_template, request, redirect, url_for, session, g
from db import get_db, close_db
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return render_template('index_user.html')
    else:
        return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/inicioUser', methods=['GET', 'POST'])
def inicioUser():
    if 'user' in session:
        return render_template('index_user.html')
    else:
        return render_template('index.html')
    
    
@app.route('/Confirmar-contraseña', methods=('GET', 'POST'))
def valid_pass():
    if 'user' in session:
        if request.method == 'POST':
            db = get_db()
            password = request.form['password']
            user = db.execute(
                'SELECT * FROM usuarios WHERE email = ?', (session['user'],)
            ).fetchone()
            store_password = user[3]
            result = check_password_hash(store_password, password)
            if result is False:
                return render_template('valid_pass.html')
            else:
                return render_template(('cambiar_pass.html'))
        else:
            return render_template('valid_pass.html')    
    else:
        return redirect(url_for('usuario'))
    

@app.route('/Cambiar-contraseña', methods=('GET', 'POST'))
def cambiar_pass():
    if 'user' in session:
        if request.method == 'POST':
            db = get_db()
            password = request.form['password']
            password2 = request.form['password2']
            if password == password2 and len(password)  >= 6 and len(password)  <= 20:
                db.execute(
                    "UPDATE usuarios SET contrasena = '%s' WHERE email ='%s'" % (generate_password_hash(password), session['user'])
                )
                db.commit()
                return redirect(url_for('logout'))
            else:
                return render_template('valid_pass.html')  
        else:
            return render_template('valid_pass.html')    
    else:
        return redirect(url_for('usuario'))
    

@app.route('/Mi-Cuenta', methods=['GET', 'POST'])
def usuario():
    if 'user' in session:
        db = get_db()
        datos = db.execute(
            'SELECT * FROM usuarios WHERE email = "%s"' % (session['user'])
        ).fetchone()
        return render_template('usuario.html', email = datos[2], name = datos[1], telefono = datos[4] , genero = datos[5], direccion = datos[6], date = datos[7])
    else:
        return redirect(url_for('index'))


@app.route( '/editar-informacion', methods=('GET', 'POST') )
def informacion():   
    if 'user' in session:
        if request.method == 'POST':
            db = get_db()
            nombre = request.form['name']
            telefono = request.form['telefono']
            genero = request.form['genero']
            direccion = request.form['direccion']
            date = request.form['date']
            datos = None
            datos = db.execute(
                "UPDATE usuarios SET nombre_usuario = '%s', email = '%s', telefono = '%s', genero = '%s', direccion = '%s', fecha_nacimiento = '%s' WHERE email='%s'" % (nombre, session['user'], telefono, genero, direccion, date, session['user'])
            )
            db.commit()
            if datos is None:
                return redirect(url_for('informacion'))
            else:
                return redirect(url_for('usuario'))  
        return render_template('informacion_user.html')
    else:
        return redirect(url_for('index'))
    

@app.route( '/login', methods=('GET', 'POST') )
def login():
    try:
        if 'user' in session:
            return redirect(url_for('index'))
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
                user = db.execute(
                    'SELECT * FROM usuarios WHERE email = ?', (username,)
                ).fetchone()
                if user is None:
                    error = 'Usuario no existe'
                    return render_template('login.html')
                else:          
                    store_password = user[3]
                    result = check_password_hash(store_password, password)
                    if result is False:
                        error = 'Contraseña inválida'
                        return render_template('login.html')
                    else:
                        session.clear()
                        session['user'] = username
                        return redirect( url_for('index'))
            else:
                session.clear()
                session['user'] = username
                return redirect(url_for('index'))
        else:
            session.clear()
            return render_template('login.html')
    except Exception as e:
        print(e)
        return render_template('login.html')

#RUTAS-----------------------------------------------------------------------------------------
@app.route('/cartelera')
def cartelera():
    if 'user' in session:
        return render_template('cartelera_user.html')
    else:
        return render_template('cartelera.html')


@app.route('/funciones')
def funciones():
    if 'user' in session:
        return render_template('funciones_user.html')
    else:
        return render_template('funciones.html')


@app.route('/peliculas/venom-carnage-liberado')
def venom():
    if 'user' in session:
        return render_template('venom.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/sin-tiempo-para-morir')
def SinTiempo():
    if 'user' in session:
        return render_template('007.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/los-locos-addams-2')
def addams():
    if 'user' in session:
        return render_template('addams.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/chernobil-la-pelicula')
def viuda():
    if 'user' in session:
        return render_template('chernobil.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/el-ultimo-duelo')
def duelo():
    if 'user' in session:
        return render_template('duelo.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/rock-dog-renace-una-estrella')
def rock():
    if 'user' in session:
        return render_template('rock.html')
    else:
        return redirect(url_for('login'))


@app.route('/peliculas/peter-rabbit-conejo-en-fuga')
def peter():
    if 'user' in session:
        return render_template('peter.html')
    else:
        return redirect(url_for('login'))
#FIN RUTAS----------------------------------------------------------------------------------------------------

@app.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
    if 'admin' in session:
        return render_template('admin.html')
    else:
        return redirect(url_for('login_admin'))
    
@app.route('/logout-admin')
def logout_admin():
    session.clear()
    return redirect(url_for('login_admin'))

@app.route('/admin', methods=('GET', 'POST'))
def login_admin():
    try:
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['email']
            password = request.form['password']
            session['admin'] = username
            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render_template( 'login_admin.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'login_admin.html' )

            user = db.execute(
                'SELECT * FROM admins WHERE UserAdmin = ? AND PassAdmin = ? ', (username, password)
            ).fetchone()      

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                return redirect(url_for('dashboard'))
            flash( error )
        return render_template('login_admin.html')
    except:
        return render_template('login_admin.html')


@app.route( '/register', methods=('GET', 'POST') )
def register():
        if request.method == 'POST':
            nombre= request.form['nombre']
            apellido= request.form['apellido']
            correo = request.form['email1']
            correo2 = request.form['email2']
            password = request.form['password']
            name = nombre +" "+ apellido
            db = get_db()
            
            if db.execute(
                'SELECT id FROM usuarios WHERE email = ?', (correo,)
                ).fetchone() is not None:
                error = 'El correo ya existe'.format(correo)
                flash( error )
                return render_template( 'register.html' )
            
            else: 
                (correo == correo2 and len(password)  >= 6 and len(password)  <= 20)               
                db.execute(
                    "INSERT INTO usuarios (nombre_usuario, email, contrasena, user,administrador) VALUES ('%s','%s','%s','SI','NO')" % (name, correo, generate_password_hash(password))
                )
                db.commit()
                #alert
                success_message = 'Usuario Registrado con el nombre de: '+ name +' correo: ' + correo +' fue registrado con exito. '
                flash(success_message)
                #fin alert
                return redirect(url_for('login'))
        return render_template( 'register.html' )

@app.route( '/registro_usuario', methods=('GET', 'POST') )
def registro_usuario():
        if request.method == 'POST':
            name= request.form['nombreCreacion']
            correo = request.form['correoCreacion']
            password = request.form['contrasena1Creacion']
            db = get_db()
            db.execute(
                "INSERT INTO usuarios (nombre_usuario, email, contrasena, user,administrador) VALUES ('%s','%s','%s','SI','NO')" % (name, correo, generate_password_hash(password))
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
                "UPDATE usuarios SET nombre_usuario = '%s', contrasena = '%s' WHERE email ='%s'" % (nombre ,password , correo)
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