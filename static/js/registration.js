function question(event) {
  event.preventDefault();
  var username = document.getElementById("userName").value;
  var password = document.getElementById("userPassword").value;
  console.log(username);
  console.log(passeord);
  const request = new XMLHttpRequest();
  request.open(
    "POST",
    `/data/${JSON.stringify({ Name: username, PWS: password })}`
  );
  request.send();
}
