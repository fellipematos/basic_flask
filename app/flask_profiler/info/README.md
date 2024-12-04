# Flask-profiler

##### Flask-profiler mede endpoints definidos no seu aplicativo Flask; e fornece relatórios detalhados por meio de uma interface web.

Ele fornece respostas para estas perguntas:
* Onde estão os gargalos no meu aplicativo?
* Quais endpoints são os mais lentos no meu aplicativo?
* Quais são os endpoints mais frequentemente chamados?
* O que causa meus endpoints lentos? Em qual contexto, com quais args e kwargs eles são lentos?
* Quanto tempo uma solicitação específica levou?

Resumindo, se você está curioso sobre o que seus endpoints estão fazendo e quais solicitações eles estão recebendo, experimente o flask-profiler.

Com a interface web do flask-profiler, você pode monitorar o desempenho de todos os seus endpoints e investigar endpoints e solicitações recebidas por meio de filtros.

## Screenshots

A visualização do painel exibe um resumo.

![Alt text](dashboard_screen.png?raw=true "Dashboard view")

Você pode criar filtros para investigar determinados tipos de solicitações.

![Alt text](filtering_all_screen.png?raw=true "Filtering by endpoint")

![Alt text](filtering_method_screen.png?raw=true "Filtering by method")

Você pode ver todos os detalhes de uma solicitação.

![Alt text](filtering_detail_screen.png?raw=true "Request detail")

## Quick Start
É fácil entender o flask-profiler passando por um exemplo. Vamos mergulhar.

Instale o flask-profiler pelo pip.
```sh
pip install flask_profiler
```


Edite seu código onde você está criando o aplicativo Flask.
```python
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

```

Agora execute seu `app.py`
```
python app.py
```

E faça alguns requests para API como:
```sh
curl http://127.0.0.1:5000/products
curl http://127.0.0.1:5000/product/123
curl -X PUT -d arg1=val1 http://127.0.0.1:5000/product/123
```

Se tudo estiver ok, o Flask-profiler medirá essas solicitações. Você pode ver o resultado indo para **http://127.0.0.1:5000/flask-profiler/** ou obter resultados como JSON http://127.0.0.1:5000/flask-profiler/api/measurements?sort=elapsed,desc

Se você gosta de inicializar suas extensões em outros arquivos ou usar o padrão de aplicativos de fábrica, você também pode criar uma instância da classe `Profiler`, isso registrará todos os seus endpoints assim que seu aplicativo for executado pela primeira vez. Por exemplo:

```python
from flask import Flask
from flask_profiler import Profiler

profiler = Profiler()

app = Flask(__name__)

app.config["DEBUG"] = True

# Você precisa declarar a configuração necessária para inicializar
# flask-profiler da seguinte forma:
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

profiler = Profiler()  # Você pode ter isso em outro módulo
profiler.init_app(app) # Ou apenas Profiler(app)

@app.route('/product/<id>', methods=['GET'])
def getProduct(id):
    return "product id is " + str(id)

```

## Usando com diferentes sistemas de banco de dados
Você pode usar o flaskprofiler com sistemas de banco de dados **SqlLite**, **MongoDB**, **Postgresql**, **Mysql** ou **MongoDB**. No entanto, é fácil dar suporte a outros sistemas de banco de dados. Se você quiser ter outros, vá para a documentação de contribuição. (É muito fácil.)

### SQLite
Para usar o SQLite, basta especificá-lo como o valor da diretiva `storage.engine` conforme a seguir.

```json
app.config["flask_profiler"] = {
    "storage": {
        "engine": "sqlite",
    }
}
```

Abaixo, as outras opções são listadas.

| Chave de filtro | Descrição | Padrão |
|----------|-------------|------|
| storage.FILE | Nome do arquivo do banco de dados SQLite | flask_profiler.sql|
| storage.TABLE | Nome da tabela na qual os dados de criação de perfil residirão | medições |

### MongoDB
Para usar o MongoDB, basta especificá-lo como o valor da diretiva `storage.engine` da seguinte forma.

```json
app.config["flask_profiler"] = {
    "storage": {
        "engine": "mongodb",
    }
}
```

### SQLAchemy
Para usar SQLAlchemy, basta especificá-lo como o valor da diretiva `storage.engine` como segue.
Crie também primeiro um banco de dados vazio com o nome "flask profiler".

```python
app.config["flask_profiler"] = {
    "storage": {
        "engine": "sqlalchemy",
        "db_url": "postgresql://user:pass@localhost:5432/flask_profiler"  # opcional, se nenhum db_url for especificado, o sqlite será usado.
    }
}
```

### Mecanismo de banco de dados personalizado
Especifique o mecanismo como módulo de string e caminho de classe.

```json
app.config["flask_profiler"] = {
    "storage": {
        "engine": "custom.project.flask_profiler.mysql.MysqlStorage",
        "MYSQL": "mysql://user:password@localhost/flask_profiler"
    }
}
```

As outras opções estão listadas abaixo.

| Chave de filtro | Descrição | Padrão
|----------|-------------|------
| storage.MONGO_URL | string de conexão mongodb | mongodb://localhost
| storage.DATABASE | nome do banco de dados | flask_profiler
| storage.COLLECTION | nome da coleção | medidas

### Amostragem
Controle o número de amostras coletadas pelo flask-profiler

Você gostaria de ter controle sobre quantas vezes o flask profiler deve coletar amostras enquanto estiver em execução no modo de produção.
Você pode fornecer uma função e controlar a amostragem de acordo com sua lógica de negócios.

Exemplo 1: Amostra 1 em 100 vezes com números aleatórios
```python
app.config["flask_profiler"] = {
    "sampling_function": lambda: True if random.sample(list(range(1, 101)), 1) == [42] else False
}
```

Exemplo 2: Amostra para usuários específicos
```python
app.config["flask_profiler"] = {
    "sampling_function": lambda: True if user is 'divyendu' else False
}
```

Se a função de amostragem não estiver presente, todas as solicitações serão amostradas.

### Alterando a raiz do endpoint do flask-profiler
Por padrão, podemos acessar o flask-profiler em <your-app>/flask-profiler

```python
app.config["flask_profiler"] = {
        "endpointRoot": "secret-flask-profiler"
}
```

### Endpoints ignorados
O Flask-profiler tentará rastrear cada ponto final definido até o momento quando init_app() for invocado. Se você quiser excluir alguns dos pontos finais, você pode definir regex correspondente para eles da seguinte forma: 

```python
app.config["flask_profiler"] = {
        "ignore": [
	        "^/static/.*",
	        "/api/users/\w+/password"
        ]
}
```

## Referencia
* [Projeto Original](https://github.com/muatik/flask-profiler/tree/master)

