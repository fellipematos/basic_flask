from flask_admin import Admin

admin = Admin()

def init_app(app):
    admin.name = "Flask Snnipets"
    admin.template_mode = "Bootstrap4"

    admin.init_app(app)