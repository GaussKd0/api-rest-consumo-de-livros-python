function exibirLivros(livros) {
    const listaLivros = document.getElementById('livros-lista');
    listaLivros.innerHTML = '';

    livros.forEach(livro => {
        const itemLista = document.createElement('li');
        itemLista.classList.add('livro-item');

        const img = document.createElement('img');
        img.src = `data:image/jpeg;base64,${livro.img}`;
        img.alt = livro.titulo;

        const nomeLivro = document.createElement('p');
        nomeLivro.classList.add('livro-nome');
        nomeLivro.textContent = livro.titulo;

        const nomeAutor = document.createElement('p');
        nomeAutor.classList.add('livro-autor');
        nomeAutor.textContent = livro.autor;

        itemLista.appendChild(img);
        itemLista.appendChild(nomeLivro);
        itemLista.appendChild(nomeAutor);
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