if (window.location.pathname.endsWith("home.html") && localStorage.getItem("loggedIn") !== "true") {
  window.location.href = "index.html";
}

const user = JSON.parse(localStorage.getItem("user"));

if (user && user.username) {
  document.getElementById("oopername").textContent = user.username;
} else {
  document.getElementById("oopername").textContent = "Guest";
}


// --------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------------------------------

function loadNotes() {
  document.getElementById("contentFrame").src = "notes.html";
}

function loadSyllabus() {
  document.getElementById("contentFrame").src = "syllabus.html";
}

window.addEventListener("load", () => {
  const iframe = document.getElementById("contentFrame");
});

function callGossip() {
  //calls various misc.
}

