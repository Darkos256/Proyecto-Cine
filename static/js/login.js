const inputs = document.querySelectorAll(".input");

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
	var cambio2 = document.getElementById("password2");
	if(cambio.type == "password"){
		cambio.type = "text";
		$('.icon').removeClass('fas fa-eye-slash').addClass('fas fa-eye');
	}else{
		cambio.type = "password";
		$('.icon').removeClass('fas fa-eye').addClass('fas fa-eye-slash');
	}

	if(cambio2.type == "password"){
		cambio2.type = "text";
		$('.icon').removeClass('fas fa-eye-slash').addClass('fas fa-eye');
	}else{
		cambio2.type = "password";
		$('.icon').removeClass('fas fa-eye').addClass('fas fa-eye-slash');
	}
} 
/*
function ShowPassword(){
	var tipo = document.getElementById("password");
	tipo.type = "text";
}

function HidePassword(){
	var tipo = document.getElementById("password");
		tipo.type = "password";
}
*/
inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});

function inicio(){
    location.href("/");
}