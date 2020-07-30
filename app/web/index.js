function submitUsername(){
    var username = document.getElementById("usernameInput").value;
    console.log(username);

    var myURL = "/checkUsername";

    $.ajax({
        type: "GET",
        url: myURL,
        data:  {'username':username},
        async: true
    });
}