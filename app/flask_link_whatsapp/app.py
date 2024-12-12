from flask import Flask
from flask import request, render_template


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
        return render_template("index.html", link=link)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()