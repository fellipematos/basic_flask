from flask import Flask

#importar admin
from admin import admin

def create_app():
    app = Flask(__name__)

    admin.init_app(app)
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean" #https://bootswatch.com/

    @app.route("/")
    def index():
        return "200 OK <BR><BR> <a href='/admin'><button>ADMIN</button></a>"
    
    return app

if __name__ == "__main__":
    app.run()