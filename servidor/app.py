from flask import Flask, render_template, request, redirect, url_for, session
import threading
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from bot.bot import start_bot

app = Flask(__name__)
app.secret_key = "luddiny_secret_key_2804"

# ========= BOT =========
def run_bot():
    start_bot()

# iniciar bot en segundo plano
# bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread = threading.Thread(target=run_bot, daemon=True)
# bot_thread.start()
bot_thread.start()

# =======================

USER = "LUDDINY"
PASS = "2804"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")

        if user == USER and password == PASS:
            session["user"] = user
            return redirect(url_for("dashboard"))

        return "Credenciales incorrectas"

    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/accion/<tipo>", methods=["POST"])
def ejecutar(tipo):
    if "user" not in session:
        return redirect(url_for("login"))

    resultado = start_bot(tipo)
    return {"resultado": resultado}

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

