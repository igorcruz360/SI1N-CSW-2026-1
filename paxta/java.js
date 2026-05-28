const datadenacimentoinput = document.getElementById ("botao");
const aniversario = document.getElementById ("aniversario");
const resultado = document.getElementById ("resultado");


function calculadoradeidade(){
    const aniversarivalor = aniversario.value;
    if(
        aniversarivalor ===""
    ){
        alert("coloca uma data certa ai po");
    } else {
        const idade = getIdade (aniversarivalor);
        resultado.innerText = 'sua idade ${idade} ${age > 1 ?  "anos" : "ano"}' ;
    }


    function getIdade(aniversarivalor) {
        const currentDAte = new Date()
        const aniversarioDAte = new Date (aniversarivalor)
        let age = currentDAte.getFullYear() - aniversarioDAte.getFullYear();
        const month = currentDAte.getMonth() - aniversarioDAte.getMonth();

        if{
            month<0 || (month === 0  && currentDAte.getDate()
        < aniversarioDAte.getDate)
        age --
        }
        return  idade;
    }
}