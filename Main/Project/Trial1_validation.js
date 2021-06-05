
/*function getName(){
  var name=document.getElementById("username").value;
  alert(name);
}*/


function getDoc(d){
    var XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("REQUEST").innerHTML = XHR.responseText;
      }
    };
    if(d==1){
      XHR.open("GET", "User_Login.html", true);
    }else{
      XHR.open("GET", "User_Register.html", true);  
    }
    XHR.send();
}

function checkForm() {
    var username = document.getElementById("username").value;
    var pwd1 = document.getElementById("pwd1").value;
    var pwd2 = document.getElementById("pwd2").value;
    console.log(username);
    if (username == "") {
        alert("Error: Username cannot be blank!");
        document.getElementById("username").focus();
        return false;
    }
    if (pwd1 != "" && pwd1 == pwd2) {
        if (pwd1.length < 6) {
            alert("Error: Password must contain at least six characters!");
            document.getElementsByName("pwd1").focus();
            return false;
        }
        if (pwd1 == username) {
            alert("Error: Password must be different from Username!");
            document.getElementById("pwd1").focus();
            return false;
        }
        re = /[0-9]/;
        if (!re.test(pwd1)) {
            alert("Error: password must contain at least one number (0-9)!");
            document.getElementById("pwd1").focus();
            return false;
        }
        re = /[a-z]/;
        if (!re.test(pwd1)) {
            alert("Error: password must contain at least one character (a-z)!");
            document.getElementById("pwd1").focus();
            return false;
        }

    } else {
        alert("Error: Please check that you've entered and confirmed your password correctly!");
        document.getElementById("pwd1").focus();
        return false;
    }

    alert("You entered a valid password, password saved successfully");
    return true;
}

