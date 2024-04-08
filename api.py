from flask import Flask, jsonify, request
from livros import livros

app = Flask(__name__)


@app.route("/livros", methods=["GET"])
def get_todos():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'error': 'Livro não encontrado'}), 404

@app.route("/livros", methods=["POST"])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_by_id(id):
    livro_novo = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[i].update(livro_novo)
            return jsonify(livros[i])
    return jsonify({'error': 'Livro não encontrado'}), 404

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro_by_id(id):
    for i, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[i]
            return jsonify({'message': 'Livro deletado com sucesso'})
    return jsonify({'error': 'Livro não encontrado'}), 404

if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)