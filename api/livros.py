import base64


livros = [
    {
        'id': 1,
        'titulo': "Clean Code",
        'autor': "Uncle Bob",
        'img': "base64_encoded_data_clean_code"
    },
    {
        'id': 2,
        'titulo': "The Pragmatic Programmer",
        'autor': "Andrew Hunt, David Thomas",
        'img': "base64_encoded_data_pragmatic_programmer"
    },
    {
        'id': 3,
        'titulo': "Design Patterns: Elements of Reusable Object-Oriented Software",
        'autor': "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        'img': "base64_encoded_data_design_patterns"
    },
]

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    return encoded_string.decode('utf-8')


livros[0]['img'] = encode_image_to_base64('imagens/clean.jpg')
livros[1]['img'] = encode_image_to_base64('imagens/pragmatic.jpg')
livros[2]['img'] = encode_image_to_base64('imagens/design.jpg') 