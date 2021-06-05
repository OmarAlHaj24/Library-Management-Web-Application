

function getName(){
  var name=document.getElementById("username").value;
  alert(name);
}

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
