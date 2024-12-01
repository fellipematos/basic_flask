from flask import Blueprint

bp_blueprint = Blueprint("blueprint", __name__, template_folder="templates", static_folder="static")

@bp_blueprint.route("/blueprint")
def blueprint():
    return "200 OK <BR><BR> BLUEPRINT <BR><BR> <a href='/'><button>Voltar</button></a>"