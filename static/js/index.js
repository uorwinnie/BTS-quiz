function question() {
  let name = prompt("What's your name?");
  let email = prompt("What is your email address?");
  let amount = prompt("How many tickets do you want to buy?");
  if (amount > 3) {
    alert(`Sorry, ${name} , you can't buy so many tickets at once.`);
  } else {
    if (amount <= 0) {
      alert(
        `${name}, you will be banned from this site if you do like this again.`
      );
    } else {
      alert(
        `Hello, ${name}! We will contect you through your emaill for detail!`
      );
    }
  }
  console.log(name);
  console.log(email);
  console.log(amount);
  const request = new XMLHttpRequest();
  request.open(
    "POST",
    `/info/${JSON.stringify({ Name: name, Email: email, Amount: amount })}`
  );
  request.send();
}
