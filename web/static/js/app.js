function login() {
  const user = document.getElementById("user").value;
  const pass = document.getElementById("pass").value;
  const msg = document.getElementById("msg");

  if (user === "LUDDINY" && pass === "2804") {
    msg.style.color = "lime";
    msg.innerText = "Acceso concedido...";
    setTimeout(() => {
      window.location.href = "dashboard.html";
    }, 800);
  } else {
    msg.style.color = "red";
    msg.innerText = "Usuario o contraseña incorrectos";
  }
}

/* =========================
   FUNCIONES DEL DASHBOARD
========================= */

function genAction() {
  alert("✨ GEN ejecutado correctamente");
  updateStatus("GEN ejecutado ✅");
}

function massAction() {
  alert("💳 MASS ejecutado correctamente");
  updateStatus("MASS ejecutado ✅");
}

function estrassAction() {
  alert("🔥 ESTRASS ejecutado correctamente");
  updateStatus("ESTRASS ejecutado ✅");
}

function updateStatus(text) {
  const status = document.getElementById("status");
  if (status) {
    status.innerText = "⚙️ Estado: " + text;
  }
}



