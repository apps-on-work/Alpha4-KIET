function signup(event) {
  event.preventDefault();

  const form = event.target;
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const username = document.getElementById("username").value;
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  const user = { username, email, password };

  localStorage.setItem("user", JSON.stringify(user));
  localStorage.setItem("loggedIn", "true");

  window.location.href = "home.html";
}


function login(event) {
  event.preventDefault();

  const form = event.target;
  if (!form.checkValidity()) {
    form.reportValidity();
    return;
  }

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const user = JSON.parse(localStorage.getItem("user"));

  if (!user) {
    document.getElementById("error").innerText =
      "No user found. Please sign up first.";
    return;
  }

  if (user.email === email && user.password === password) {
    localStorage.setItem("loggedIn", "true");
    window.location.href = "home.html";
  } else {
    document.getElementById("error").innerText =
      "Invalid login credentials";
  }
}


function logout() {
  localStorage.setItem("loggedIn", "false");
  window.location.href = "index.html";
}
