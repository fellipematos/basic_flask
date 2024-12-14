from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        base_url = "https:/wa.me/"
        whatsapp = request.form["whatsapp"]
        mensagem = request.form["mensagem"].replace(" ", "%20")

        def clear(whatsapp):
            for char in " -()":
                whatsapp = whatsapp.replace(char, "")
            return whatsapp

        link = f"{base_url}+55{clear(whatsapp)}?text={mensagem}"
        return f"""
            <P>{link}</P>
            <BR><BR>
            <a href='/'><button>VOLTAR</button></a>
            """
    return """
        <form action="" method="post">
            <input type="text" name="whatsapp" placeholder="Insira seu numero de Whatsapp: ex.:DDD900000000"><BR><BR>
            <textarea name="mensagem" placeholder="Digite a mensagem padrão:"1 rows="3" cols="32"></textarea><BR><BR>
            <input type="submit" value="GERAR LINK">
        </form>
        """

if __name__ == "__main__":
    app.run()