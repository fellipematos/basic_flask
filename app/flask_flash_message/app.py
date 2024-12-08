from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "flask_flash"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form["flag"].upper() != "FLAG":
            flash("FLAG Inválida!")
        else:
            flash("FLAG Encontrada!")
        return redirect(url_for("index"))
    return render_template('index.html')
