if (window.location.pathname.endsWith("index.html") && localStorage.getItem("loggedIn") !== "true") {
  window.location.href = "login.html";
}

const user = JSON.parse(localStorage.getItem("user"));

if (user && user.username) {
  document.getElementById("oopername").textContent = user.username;
} else {
  document.getElementById("oopername").textContent = "Guest";
}
