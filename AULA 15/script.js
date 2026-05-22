var issoeumastring = "Isso é uma string";
var issoeumnumero = 42;
var issoeumbooleano = true;

console.log(issoeumastring);
console.log(issoeumnumero);
console.log(issoeumbooleano)

var issotambemeumastring ="42";

if (issoeumnumero == issotambemeumastring) {
    console.log ("as strings são iguais");
} else {
    console.log ("as strings são diferentes");
}
if (issoeumastring == issotambemeumastring) {
    console.log ("o número e a string são iguais"); 
} else{
    console.log ("o número e a string são diferentes")
}

let idade = 16 
console.log(idade <15 ? "criança" : "adulto")

if(idade  <15) {
    console.log("criança")
} else if (idade <25) {
    console.log("jovem")
}else if (idade <60){
    console.log ("adulto")
}else{
    console.log("idoso")
}

let dia =3
let diaextenso =""
switch (dia){
    case 1: diaextenso = "domingo"; break;
    case 2: diaextenso = "segunda"; break;
    case 3: diaextenso = "terça"; break;
    case 4: diaextenso = "quarta"; break;
    case 5: diaextenso = "quinta"; break;
    case 6: diaextenso = "sexta"; break;
    default: diaextenso = "sabado"
}
console.log(diaextenso)

for (var i=0; i <= 5; i++)
{
    console.log(i)
}

var j=0
while (j<=5){
    console.log(j);
    j++;
}

for (var i=0; i< 11; i++) {
    if (i%2===0){
        console.log(i)}   
}
