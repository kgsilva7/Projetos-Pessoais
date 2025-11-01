const imagemVizualizacao = document.querySelector("#vizualizacao img");
let numImagemSelecionada = 1;
function atualizarImagemSelecionada() {
    const opcaoImagemSelecionada = document.querySelector(
    '[name="opcoes-imagem"]:checked' //selecionado todos que tiverem essa opcão marcada
    ).id.charAt(); //pegando o id da imagem selecionada com a posição do elemento
    numImagemSelecionada = opcaoImagemSelecionada; //número da imagem tem que ser igual a selecionada
  imagemVizualizacao.src = 
  "./imagens/opcoes-cores/imagens-azul-inerno/imagem-" + 
  numImagemSelecionada 
  ".jpeg"; //seleciona a imagem e a cor
}   
atualizarImagemSelecionada(); //para executar a imagem selecionada