function verificar() {
			
    email1 = document.PruebaFormulario.email1.value
    email2 = document.PruebaFormulario.email2.value
    contrasena = document.PruebaFormulario.password.value
    error1 = null
    error2 = null

    // Verificamos si las constraseñas no coinciden 
    if (email1 != email2) {
        error1 = true
    }

    if(contrasena.length  < 6 || contrasena.length  > 12){
        error2 = true
    }

    // Si los correos no coinciden mostramos un mensaje
    if(error1 == true){
        alert("Los correos NO son iguales \nPor Favor ingrese el mismo correo de verificación")
    }

    // Si la contraseña no tiene mas de 6 caracteres y menos de 12 es invalida
    else if(error2 == true){
       
        alert("Contraseña Invalida\n Una contraseña valida debe tener mas de 6 caracteres y menos de 12...") 
    }

    // Si las contraseñas son validas y los correos correctos coinciden mostramos un mensaje
    else {
        alert("Validaciones exitosas \nCargando pagina...") 
    }
}