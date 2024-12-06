import os
from flask import Flask, request, redirect, url_for, render_template, flash

# Configurações básicas
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'docx'}

app = Flask(__name__)
app.secret_key = 'uploaddearquivo'  # Necessário para usar flash messages
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verifica se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota principal com formulário de upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado
        if 'file' not in request.files:
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = file.filename
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            flash(f'Arquivo {filename} enviado com sucesso!')
            return redirect(url_for('upload_file'))
        else:
            flash('Tipo de arquivo não permitido')
            return redirect(request.url)
    
    return render_template('upload.html')

# Inicialização do servidor
if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Garante que o diretório existe
    app.run(debug=True)
