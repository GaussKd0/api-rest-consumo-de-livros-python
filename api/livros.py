import base64

livros = [
    {
        'id': 1,
        'titulo': "Clean Code",
        'autor': "Uncle Bob",
        'imagem_path': 'imagens/clean.jpg'
    },
    {
        'id': 2,
        'titulo': "The Pragmatic Programmer",
        'autor': "Andrew Hunt, David Thomas",
        'imagem_path': 'imagens/pragmatic.jpg'
    },
    {
        'id': 3,
        'titulo': "Design Patterns: Elements of Reusable Object-Oriented Software",
        'autor': "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        'imagem_path': 'imagens/design.jpg'
    },
    {
        "id": 4,
        "titulo": "O Chamado De Cthulhu",
        "autor": "H. P. Lovecraft",
        'imagem_path': 'imagens/cathulhu.jpg'
    },
  
]

def adicionar_imagem_base64(livro):
    imagem_path = livro.get('imagem_path')
    with open(imagem_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    livro['img'] = encoded_string.decode('utf-8')
    return livro

def adicionar_imagens_base64_aos_livros(livros):
    return [adicionar_imagem_base64(livro) for livro in livros]

livros = adicionar_imagens_base64_aos_livros(livros)
