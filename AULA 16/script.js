document.writeln('OLÁ MUNDO!!');

window.alert("olá mundo, seu lindo!!");

document.getElementById('titulo').innerHTML = "olá mundo javascript";

let nomePrompt = window.prompt("ola aluno de js, qual é seu nome?")

document.writeln("o nome do aluno js é: " + nomePrompt)

document.getElementById ('nomeAluno').innerhtml = ("o nome do aluno js é : " + nomePrompt)

let resposta = window.confirm("vc gosta de js")

if (resposta) {
    document.getElementById ('respostaAluno').innerHTML = "o aluno gosta de js";

} else {
   document.getElementById ('respostaAluno').innerHTML = "o aluno não gosta de js"
}

function exibeNomeAluno() {
    let inputAluno = document.getElementById('imputNomeAluno').value;
    document.getElementById("resposta").innerHTML = "o nome digitado foi" + inputNomeAluno
}