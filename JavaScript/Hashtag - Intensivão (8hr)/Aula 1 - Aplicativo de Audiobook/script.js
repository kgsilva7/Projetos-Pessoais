// CamelCase
const botaoPlayPause = document.getElementById("play-pause"); //pega a variável no Html pelo Id
const botaoProximoCapitulo = document.getElementById("proximo"); //pega a variável no Html pelo Id
const botaocapituloAnterior = document.getElementById("anterior"); //pega a variável no Html pelo Id
const audio = document.getElementById("audio-capitulo"); //pega a variável no Html pelo Id
const textoCapitulo = document.getElementById("capitulo"); //pega a variável no Html pelo Id
const qtdeCapitulos = 10; //quantidade de capitulos
let taTocando = false; 
let capituloAtual = 1; //começa no primeiro capitulo
function tocarFaixa() { //abre uma função de tocar a faixa
    console.log("Clicou!"); //mostra se clicou
    audio.play(); //abre o áudio
    taTocando = true; //se estiver tocando
    console.log("Deu Play"); //mostra que deu play
    botaoPlayPause.classList.add("tocando") //adiciona o audio para tocar
}
function pausarFaixa() {
    console.log("Clicou!");
    audio.pause();
    taTocando = false;  
    console.log("Deu Pause");
    botaoPlayPause.classList.remove("tocando") //remove o audio
}
function tocarOuPausar() {
    if (taTocando === true) { //compara se está tocando
        pausarFaixa();
    } else { 
        tocarFaixa(); 
    }
}
function proximoCapitulo() {
    pausarFaixa()
    if (capituloAtual < qtdeCapitulos) { 
        capituloAtual = capituloAtual + 1;
    } else {
        capituloAtual = 1; //vai oltar ao primeiro
    }
    audio.src = "./audios/" + capituloAtual + ".mp3"; //trocar os audios depois das funções
    textoCapitulo.innerText = "Capítulo " + capituloAtual; //atribui as funçoes ao capitulo
}
function capituloAnterior() {
    pausarFaixa()
    if (capituloAtual === 1) {
        capituloAtual = qtdeCapitulos;
    } else {
        capituloAtual = capituloAtual - 1;
    }
    audio.src = "./audios/" + capituloAtual + ".mp3";
    textoCapitulo.innerText = "Capítulo " + capituloAtual;
}
botaoPlayPause.addEventListener("click", tocarOuPausar);
botaoProximoCapitulo.addEventListener("click", proximoCapitulo);
botaoCapituloAnterior.addEventListener("click", capituloAnterior);