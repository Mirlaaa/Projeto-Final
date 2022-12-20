$(document).ready(function () {
    $("#cpf").mask("999.999.999-99");
  });


function teste(auth) {
    const sign_in_btn = document.querySelector("#sign-in-btn");
    const sign_up_btn = document.querySelector("#sign-up-btn");
    const container = document.querySelector(".container");

    if (auth === "sign-in") {
        container.classList.remove("sign-up-mode");
    } else {
        container.classList.add("sign-up-mode");
    }
}

function loginFunc() {
    var wind = "http://localhost:8000/accounts/login";
    window.open(wind, "_parent");
}

function cadastroFunc() {
    var wind = "http://localhost:8000/accounts/cadastro";
    window.open(wind, "_parent");
}



const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");

sign_up_btn2.addEventListener("click", () => {
    container.classList.add("sign-up-mode2");
});
sign_in_btn2.addEventListener("click", () => {
    container.classList.remove("sign-up-mode2");
});


var alerta = document.getElementById("alert").innerHTML;
if (alerta != null) alert(alerta);
