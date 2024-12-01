# Flask Blueprints Básico

Este snippet demonstra como utilizar **Flask Blueprints** para organizar uma aplicação Flask em módulos. Ele é útil para projetos de qualquer tamanho e essencial para manter o código limpo e organizado em aplicações maiores.

---

## 📋 Funcionalidades

- Demonstra a criação de um **Blueprint**.
- Mostra como registrar um Blueprint na aplicação principal.
- Exemplo básico de organização de rotas por módulo.

---

## 🛠️ Biblioteca Utilizada

Certifique-se de ter a seguinte biblioteca instalada:

- **Flask**

---

## 📂 Estrutura do Projeto

flask_blueprints/
|
├── app.py # Arquivo principal da aplicação
├── readme.md # Este arquivo
    |
    ├── blueprint/
        |
        ├── init.py # Inicialização do módulo
        ├── main.py # Blueprint principal com as rotas
        ├── templates/ # Pasta para templates html do modulo 
        ├── static/ # Pasta para estilos do modulo 