const SIN = document.getElementById('signin');
const SUP = document.getElementById("signup");
const SOUT = document.getElementById("signout");


function sIn(){
    SIN.addEventListener('click', () => { 
        location.href = "login_system/templates/authentication/signin.html";
    })
}

function sUp() {
  SUP.addEventListener("click", () => {
    window.location.href = "login_system/templates/signup.html";
  });
}

function sOut() {
  SOUT.addEventListener("click", () => {
    window.location.href = "login_system/templates/signout.html";
  });
}




