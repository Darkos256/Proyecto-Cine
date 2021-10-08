const inputs = document.querySelectorAll('input');

const nombre = document.getElementById('nombre')
const apellido = document.getElementById('apellido')
const email = document.getElementById('email')
const confirmarEmail = document.getElementById('confirmar-email')
const password = document.getElementById('password')
const form = document.getElementById('form')
/*----------------------------------------------------------------*/

form.addEventListener('submit', e =>{
	e.preventDefault()
	let regexname = /^[a-zA-ZÀ-ÿ\s]{1,40}$/
	let regexemail = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
	let regexpassword = /^.{4,12}$/

	if(!regexname.test(nombre.value)){
		
	}

	if(!regexname.test(apellido.value)){

	}

	if(!regexemail.test(email.value)){

	}

	if(email.value == confirmarEmail.value){

	}else{
		alert('El correo no es igual')
	}

	if(!regexpassword.test(password.value)){
		
	}
})

/*----------------------------------------------------------------*/

function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}

function ShowHidePassword(){
	var cambio = document.getElementById("password");
	if(cambio.type == "password"){
		cambio.type = "text";
		$('.icon').removeClass('fas fa-eye-slash').addClass('fas fa-eye');
	}else{
		cambio.type = "password";
		$('.icon').removeClass('fas fa-eye').addClass('fas fa-eye-slash');
	}
} 

inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

