from flask import Flask
import flask_profiler

app = Flask(__name__)
app.config["DEBUG"] = True

#Principais configurações
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
	    "^/static/.*"
	]
}

#APPLICATION WEB
@app.route("/")
def index():
    return "200 OK <BR><BR> <a href='/flask-profiler'><button>Acessar Flask Profiler</button></a>"

#API
@app.route('/product/<id>', methods=['GET'])
def getProduct(id):
    return "product id is " + str(id)

@app.route('/product/<id>', methods=['PUT'])
def updateProduct(id):
    return "product {} is being updated".format(id)

@app.route('/products', methods=['GET'])
def listProducts():
    return "suppose I send you product list..."

@app.route('/static/something/', methods=['GET'])
def staticSomething():
    return "this should not be tracked..."

#Aqui iniciamos o flask_profile passando o app
#Todos os endpoints da API declarados até agora serão rastreados pelo flask-profiler.
flask_profiler.init_app(app)

#Endpoint declarados após flask_profiler.init_app(), são ocultos
@app.route('/doSomething', methods=['GET'])
def doSomething():
    return "flask-profiler will not measure this."

# Caso precise de um endpoint seja medido pelo flask-profiler, você pode usar o decorador profile()
@app.route('/doSomethingImportant', methods=['GET'])
@flask_profiler.profile()
def doSomethingImportant():
    return "flask-profiler will measure this request."

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)