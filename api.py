from flask import Flask, jsonify,request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titilo': "Clean Code",
        'autor': "nao sei",
    },
    {
        'id': 2,
        'titilo': "Clean Code",
        'autor': "nao sei",
    },
    
    {
        'id': 3,
        'titilo': "Clean Code",
        'autor': "nao sei",
    },
]
@app.route("/livros")
def get_todos():
    return jsonify(livros)

app.run(port=5000,host="localhost", debug=True)