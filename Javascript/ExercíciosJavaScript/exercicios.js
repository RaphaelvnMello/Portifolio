/*1- Escreva um programa que faça 7 chamadas a console.log() para retornar o seguinte 
triângulo.
#
##
###
####
#####
######
#######*/

var rcaracteres = ''

for (var i = 0; i < 7; i++) {
        rcaracteres = rcaracteres + '#' 
        console.log(rcaracteres);
}

rcaracteres = '' 

/* Escreva um programa que imprima (usando console.log()) todos os números de 1 a 100, 
exceto que, para números divisíveis por 3, ele imprima FizzBuzz ao invés do número, e 
para números divisíveis por 5 (e não 3), ele imprima Buzz. Quando você tiver o 
programa funcionando, modifique-o para imprimir Fizz para números que são divisíveis 
por ambos os números 3 e 5 (Isto é na verdade uma pergunta de entrevista usada para 
eliminar uma porcentagem significativa de candidatos programadores. Então, se você 
resolvê-la, você está autorizado de se sentir bem consigo mesmo).*/


for (var i = 0; i <= 100; i++) {

    if(i % 3 == 0 && i % 5 !=0){
        i == 0 ? console.log(i) : console.log('FizzBuzz')
    }
    else if(i % 5 == 0 && i % 3 !=0) {
        i == 0 ? console.log(i) : console.log('Buzz')
    }  
    else if(i % 5 == 0 && i % 3 == 0){
        i == 0 ? console.log(i) : console.log('Fizz')
    }
    else {
        console.log(i)
    }
}

/* 3- Escreva um programa que cria uma string que representa uma grade 8x8, usando novas 
linhas para separar os caracteres. A cada posição da grade existe ou um espaço ou um 
caracter “#”, de forma que estes caracteres formem um tabuleiro de xadrez.
Passando esta string para console.log, ela deverá se parecer com isso:
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
Quando isso funcionar, defina uma variável tamanho = 8, e mude o programa para que 
o mesmo funciona para qualquer tamanho, retornando uma grade com a largura e 
altura fornecida.*/


var grade ='';var tam = 20;


for (var i = 0; i < tam; i++) {
    for (var j = 0; j < tam; j++) {
        if(i % 2 == 0){
            if(j % 2 == 0){
                grade = grade + '#' 
            }
            else{
                grade = grade + ' ' 
            }    
        }else if (j % 2 == 0){
                grade = grade + ' ' 
        }
            else{
                grade = grade + '#' 
            } 
    }
    console.log(grade) 
    grade = ''
}
