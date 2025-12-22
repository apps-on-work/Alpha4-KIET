function signup() {
  const username = document.getElementById("username").value;
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  if (!username || !email || !password) {
    alert("Fill all fields");
    return;
  }

  const user = { username, email, password };

  localStorage.setItem("user", JSON.stringify(user));
  localStorage.setItem("loggedIn", "true");

  window.location.href = "index.html";
}

function login(event) {
  event.preventDefault();
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const user = JSON.parse(localStorage.getItem("user"));

  if (!user) {
    document.getElementById("error").innerText = "No user found. Please sign up first.";
    return;
  }

  if (user.email === email && user.password === password) {
    localStorage.setItem("loggedIn", "true");
    window.location.href = "index.html";
  } else {
    document.getElementById("error").innerText = "Invalid login credentials";
  }
}


function logout() {
  localStorage.setItem("loggedIn", "false");
  window.location.href = "login.html";
}
