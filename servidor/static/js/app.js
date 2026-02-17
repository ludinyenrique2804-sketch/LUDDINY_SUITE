function login()from flask import jsonify
from bot.bot import start_bot
 {
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
function updateStatus(text, color = "lime") {
  const status = document.getElementById("status");
  status.style.color = color;
  status.innerText = text;
}

function getFlag(country) {
  const flags = {
    "UNITED STATES": "🇺🇸",
    "USA": "🇺🇸",
    "MEXICO": "🇲🇽",
    "SPAIN": "🇪🇸",
    "DOMINICAN REPUBLIC": "🇩🇴",
    "BRAZIL": "🇧🇷",
    "ARGENTINA": "🇦🇷"
  };
  return flags[country.toUpperCase()] || "🌍";
}

function renderResult(text) {
  const box = document.getElementById("result");

  let card = text.match(/VISA|MASTERCARD|AMEX/i);
  let bank = text.match(/BANK:\s*(.*)/i);
  let country = text.match(/COUNTRY:\s*(.*)/i);

  let output = "";

  if (card) output += `💳 ${card[0]}\n`;
  if (bank) output += `🏦 Banco: ${bank[1]}\n`;
  if (country) {
    const flag = getFlag(country[1]);
    output += `🌍 País: ${country[1]} ${flag}\n`;
  }

  output += `\n${text}`;

  box.innerText = output;
}


function sendAction(cmd) {
    fetch(`/action/${cmd}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("status").innerHTML = `
                <b>✅ Estado:</b> ${data.status}<br>
                <b>💳 Tarjeta:</b> ${data.card}<br>
                <b>🏷️ Tipo:</b> ${data.type}<br>
                <b>🏦 Banco:</b> ${data.bank}<br>
                <b>🌍 País:</b> ${data.country}
            `;
        })
        .catch(() => {
            alert("❌ Error ejecutando el bot");
        });
}

