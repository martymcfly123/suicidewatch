function submitUsername(){
    var username = document.getElementById("usernameInput").value;
    console.log(username);

    window.location.href = "http://localhost:5000/userHistory";

    var myURL = "/checkUsername";


    $.ajax({
        type: "POST",
        url: myURL,
        data:  {'username':username},
        async: true
    });
}