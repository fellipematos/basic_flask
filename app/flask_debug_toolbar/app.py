from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config["SECRET_KEY"] = "debugtoolbar"

# Ativar a toolbar? (Padrão: app.debug)
#app.config["DEBUG_TB_ENABLED"] = True

# Lista de hosts permitidos para exibir a toolbar (Padrão: qualquer host)
#app.config["DEBUG_TB_HOSTS"] = ['127.0.0.1', 'localhost']

# Deve interceptar redirecionamentos? (Padrão: True)
#app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = True

# Lista de módulos/classes dos painéis (Padrão: todos os painéis internos ativados)
#app.config["DEBUG_TB_PANELS"] = [
#    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
#    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
#    'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
#]

# Ativar o profiler em todas as requisições? (Padrão: False, ativado pelo usuário)
#app.config["DEBUG_TB_PROFILER_ENABLED"] = False

# Ativar o editor de templates? (Padrão: False)
#app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = False

# Nome do arquivo de dump das estatísticas do profiler (Padrão: None, nenhum dump será gravado)
#app.config["DEBUG_TB_PROFILER_DUMP_FILENAME"] = None


app.debug = True

toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    return """
    <!--Importante o debugtoolbar, não funciona sem as tag <html> <body>-->
    <html> 
    <body>
    
    <h1>200 OK</h1>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='localhost', port=5000)