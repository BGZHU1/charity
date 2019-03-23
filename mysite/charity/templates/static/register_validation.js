$(document).ready(function () {
    $("#submit").click(function (e) {
        var firstname = document.getElementById('firstname');
        var lastname = document.getElementById('lastname');
        var password = document.getElementById('password');
        var email = document.getElementById('password');


  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  //console.log(re.test(email.value))


        if (firstname === undefined || firstname.value.length === 0) {
            //e.preventDefault();
            console.log(firstname, firstname.value)
            alert("Please input a first name");
            e.preventDefault();
        } else if (lastname === undefined || lastname.value.length === 0) {
            alert("Please input a last name");
            e.preventDefault();
        } else if (email === undefined || email.value.length === 0 /*|| re.test(email.value) === false*/) {
            alert("Please input an valid email");
            e.preventDefault();
        }  else if (password  === undefined || password.value.length === 0) {
            alert("Please input an password");
            e.preventDefault(); //this prevents redirect
        }
    });
});
