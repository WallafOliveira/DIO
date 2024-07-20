# Código do servidor Flask
flask_code = """
from flask import Flask, jsonify
import json

app = Flask(__name__)

def carregar_dados():
    try:
        with open('data.json', 'r') as file:
            dados = json.load(file)
        return dados
    except FileNotFoundError:
        return {"error": "Arquivo JSON não encontrado"}
    except json.JSONDecodeError:
        return {"error": "Erro ao decodificar o JSON"}

@app.route('/index', methods=['GET'])
def index():
    dados = carregar_dados()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
"""

# Criar o arquivo app.py
with open('app.py', 'w') as file:
    file.write(flask_code)

# Criar o arquivo data.json
with open('data.json', 'w') as file:
    json.dump([
        {"id": 1, "nome": "João Silva", "email": "joao@exemplo.com"},
        {"id": 2, "nome": "Maria Oliveira", "email": "maria@exemplo.com"}
    ], file)
