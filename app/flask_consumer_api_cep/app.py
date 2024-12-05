from flask import Flask
from flask import render_template, request
import httpx

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cep = request.form["cep"]
        search = httpx.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
        result = search.json()
        return render_template("response.html", result=result)
            

    return render_template("index.html")

if __name__ == "__main__":
    app.run()