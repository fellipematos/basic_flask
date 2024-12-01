from flask import Flask, render_template

#import blueprint
from blueprint.main import bp_blueprint


app = Flask(__name__)

#registra blueprints
app.register_blueprint(bp_blueprint)

@app.route("/")
def index():
    return "200 OK <BR><BR> <a href='/blueprint'><button>Blueprint</button></a>"

if __name__ == "__main__":
    app.run()