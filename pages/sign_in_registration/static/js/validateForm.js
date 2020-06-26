function validate() {
    var pass = document.getElementById("pwd").value;
    var cpass = document.getElementById("cpwd").value;
    if (pass == cpass) {
        return true;
    } else {
        alert("Passwords do not match");
        return false;
    }
}


