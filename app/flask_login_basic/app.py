from flask import Flask
from flask import render_template, url_for, request, redirect

from flask_login import LoginManager
from flask_login import login_user, logout_user
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

#config
app.config["SECRET_KEY"] = "flasklogin"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager(app)
db = SQLAlchemy(app)

#buscar usuario
@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

#classe de usuario
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key="True")
    name = db.Column(db.String(), nullable= False)
    email = db.Column(db.String(), nullable= False, unique=True)
    password = db.Column(db.String(), nullable= False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)

#criar tabelas no banco
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return redirect(url_for("login"))
        
        login_user(user)
        return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()