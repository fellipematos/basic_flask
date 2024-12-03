from flask import Flask
from flask import render_template, url_for, request, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#config
app.config["SECRET_KEY"] = "flaskcrudsqlalchemy"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

#classe model 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key="True")
    name = db.Column(db.String(), nullable= False)
    code = db.Column(db.String(), nullable= False)

    def __init__(self, name, code):
        self.name = name
        self.code = code

#criar tabelas no banco
with app.app_context():
    db.create_all()

#CREATE
@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user = User(request.form["name"], request.form["code"])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("read_user"))
    return render_template("create.html")

#READ
@app.route("/")
def read_user():
    user = User.query.all()
    return render_template("index.html", user=user)

#UPDATE
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User.query.get(id)
    if request.method == "POST":
        user.name = request.form["name"]
        user.code = request.form["code"]
        db.session.commit()
        return redirect(url_for("read_user"))
    return render_template("update.html", user=user)

#DELETE
@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("read_user"))

if __name__ == "__main__":
    app.run()