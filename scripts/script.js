function exibirLivros(livros) {
    const listaLivros = document.getElementById('livros-lista');
    listaLivros.innerHTML = '';

    livros.forEach(livro => {
        const itemLista = document.createElement('li');
        const img = document.createElement('img');
        img.src = `data:image/jpeg;base64,${livro.img}`;
        img.alt = livro.titulo;
        const textoLivro = document.createTextNode(`${livro.titulo} - ${livro.autor}`);
        itemLista.appendChild(img);
        itemLista.appendChild(textoLivro);
        listaLivros.appendChild(itemLista);
    });
}

function filtrarLivros(livros, termo) {
    return livros.filter(livro => livro.titulo.toLowerCase().includes(termo.toLowerCase()));
}

function carregarLivros() {
    fetch('http://localhost:5000/livros', { mode: 'cors' })
        .then(response => response.json())
        .then(data => {
            exibirLivros(data);
            adicionarEventoFiltro(data);
        })
        .catch(error => console.error('Erro ao carregar livros:', error));
}

function adicionarEventoFiltro(livros) {
    const filtroInput = document.getElementById('filtro');
    filtroInput.addEventListener('input', function() {
        const termo = this.value.trim();
        const livrosFiltrados = filtrarLivros(livros, termo);
        exibirLivros(livrosFiltrados);
    });
}

window.onload = carregarLivros;