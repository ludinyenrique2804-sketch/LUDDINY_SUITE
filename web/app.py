from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "luddiny_secret_key_2804"

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
        else:
            return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


