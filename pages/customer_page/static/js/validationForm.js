function validate() {
    var pass = document.getElementById("npwd").value;
    var cpass = document.getElementById("npwd2").value;
    if (pass == cpass) {
        return true;
    } else {
        alert("Passwords do not match");
        return false;
    }
}

