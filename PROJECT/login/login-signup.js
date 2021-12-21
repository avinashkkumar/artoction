var x= document.getElementById("login");
var y= document.getElementById("signup");
var z= document.getElementById("btn");

function signup()
{
    x.style.left="-30rem";
    y.style.left="2.4rem";
    z.style.left="6.8em";

}
function login()
{
    x.style.left="2.5rem";
    y.style.left="32.4rem";
    z.style.left="0";

}

//password validation

function Validate() {
    var password = document.getElementById("txtPassword").value;
    var confirmPassword = document.getElementById("txtConfirmPassword").value;
    if (password != confirmPassword) {
        alert("Passwords do not match.Try Again!");
        return false;
    }
    return true;
}
