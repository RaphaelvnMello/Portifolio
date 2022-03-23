//Primeira questão
var numero = 0;

numero = prompt("Insira um número: ");

var resposta = espelhar(numero);

console.log(resposta);

// Função
function espelhar(numero) {

var inverso = [];

numeroString = numero.toString();

for (var i = 0; i < numeroString.length; i++){

    inverso[i] = numeroString[(numeroString.length-1) - i];
}

var inversoString = inverso.toString();

for (var i = 0; i < inversoString.length; i++)
if(inversoString[i] === ','){
    inversoString = inversoString.replace(',','');
}

var resposta = Number(inversoString);


return resposta;
}




