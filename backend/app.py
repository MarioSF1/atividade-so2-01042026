from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from backend!"}), 200

list_of_clients = [
    {"id": 1, "name": "mario", "email": "mario@mario.com"},
    {"id": 2, "name": "maicon", "email": "maicon@maicon.com"}
]

@app.route('/listar-clientes', methods=['GET'])
def listar_clientes():
    return jsonify(list_of_clients), 200

list_of_employees = [
    {"id": 1, "name": "mario trabalhador", "email": "mario@trabalhador.com"},
    {"id": 2, "name": "maicon trabalhador", "email": "maicon@trabalhador.com"}
]


@app.route('/listar-funcionarios', methods=['GET'])
def listar_funcionarios():
    return jsonify(list_of_employees), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)