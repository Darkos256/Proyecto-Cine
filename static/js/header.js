const menuIcon = document.querySelector(".hamburger-menu");
const navbarRigh = document.querySelector(".navbar-righ");

menuIcon.addEventListener("click", () => {
    navbarRigh.classList.toggle("change-righ");
});

const menuUser = document.querySelector(".hamburger-menu2");
const navbarLeft = document.querySelector(".navbar-left");

menuUser.addEventListener("click", () => {
    navbarLeft.classList.toggle("change-left");
});
