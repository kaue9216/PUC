// 1. Maioridade
// Crie uma variável chamada idade e atribua a ela a idade de uma pessoa. Utilize if...else para verificar se a pessoa é maior ou menor de idade. Ao final, exiba uma mensagem informando a idade e a situação da pessoa, utilizando interpolação de strings.

let idade = 17;
let nome = 'ana';

if (idade >= 18){
    console.log(`${nome} tem ${idade} anos e é maior de idade`);
}else {
    console.log(`${nome} tem ${idade} anos e é menor de idade`);
}

// -----------------------------------------------------------------

// 2. Aprovação do aluno
// Crie as variáveis nome e nota. Verifique, utilizando if...else, se o aluno foi aprovado ou reprovado. Considere que a nota mínima para aprovação é 7. Exiba uma mensagem contendo o nome do aluno, sua nota e sua situação, utilizando interpolação.

let nome = 'ana';
let nota = 6;
if (nota >= 7){
    console.log(`${nome} tirou ${nota} e passou de ano`);
} else {
    console.log(`${nome} tirou ${nota} e reprovou`);
}

// -----------------------------------------------------------------

// 3. Número positivo ou negativo
// Crie uma variável chamada numero. Utilize if...else para verificar se o número informado é positivo ou negativo. Ao final, apresente uma mensagem contendo o número e o resultado da verificação utilizando interpolação.

let numero = -6;
if (numero > 0){
    console.log(`${numero} é positivo`);
} else {
    console.log(`${numero} é negativo`);
}

// -----------------------------------------------------------------

// 4. Verificação de temperatura
// Crie uma variável chamada temperatura para armazenar uma temperatura em graus Celsius. Utilize if...else para verificar se a temperatura é maior ou igual a 30 °C. Caso seja, informe que está quente; caso contrário, informe que a temperatura está agradável. A mensagem deverá utilizar interpolação.

let temperatura = 31;
if (temperatura >= 30){
    console.log(`${temperatura} garus é quente`);
} else {
    console.log(`${temperatura} garus é agradável`);
}

// -----------------------------------------------------------------

// 5. Aumento salarial
// Crie as variáveis nome e salario. Verifique se o salário da pessoa é inferior a R$ 2.500,00. Caso seja, informe que ela receberá um aumento de 10%. Caso contrário, informe que ela não receberá aumento. Exiba o nome, o salário e a situação utilizando interpolação.

let salario = 2501;
if (salario <= 2500){
    console.log(`seu salário é ${salario} você receberá um aumento de 10%, seu salário passou para ${salario * 1.1}`);
} else {
    console.log(`seu salário é ${salario} você não receberá um aumento`);
}


// -----------------------------------------------------------------

// 6. Verificação de senha
// Crie as variáveis senhaCadastrada e senhaDigitada. Utilize if...else para verificar se a senha digitada é igual à senha cadastrada. Caso seja igual, informe que o acesso foi autorizado; caso contrário, informe que a senha está incorreta. A mensagem deverá utilizar interpolação.


let senhaCadastrada = '*****';
let senhaDigitada = '****';
if (senhaCadastrada === senhaDigitada){
    console.log(`voce digitou a senha ${senhaDigitada}, ela é a senha correta`);
} else {
    console.log(`voce digitou a senha errada`);
}

// -----------------------------------------------------------------

// 7. Desconto em uma compra
// Crie as variáveis produto e preco. Verifique se o preço do produto é superior a R$ 100,00. Caso seja, aplique um desconto de 10%. Caso contrário, mantenha o preço original. Ao final, exiba o nome do produto, o preço original e o preço final utilizando interpolação.

let produto = 'bala 7 belos';
let preco = 10;
if (preco >= 100){
    console.log(`voce recebeu um desconto de 10% no produto ${produto} o novo preço é ${preco * 0.9}`);
} else {
    console.log(`voce não vai receber desconto no produto ${produto}`);
}

// -----------------------------------------------------------------

// 8. Classificação por idade
// Crie uma variável chamada idade. Utilize if...else if...else para classificar uma pessoa de acordo com sua idade: de 0 a 12 anos como criança, de 13 a 17 anos como adolescente, de 18 a 59 anos como adulto e 60 anos ou mais como idoso. Ao final, apresente uma mensagem contendo a idade e a classificação utilizando interpolação.

let idade = 13;
if (idade >= 60){
    console.log(`voce tem ${idade} anos, voce é um idoso`);
} else if (idade >= 18){
    console.log(`voce tem ${idade} anos, voce é um adulto`);
} else if (idade >= 12){
    console.log(`voce tem ${idade} anos, voce é um adolescente`);
} else {
    console.log(`voce tem ${idade} anos, voce é uma criança`);
}

// -----------------------------------------------------------------


// 9. Média de três notas
// Crie as variáveis nome, nota1, nota2 e nota3. Calcule a média das três notas e utilize if...else if...else para determinar a situação do aluno: média maior ou igual a 7, aprovado; média entre 5 e 6,9, recuperação; média inferior a 5, reprovado. Exiba o nome, as notas, a média e a situação utilizando interpolação.

let nome = 'icaro';
let nota1 = 10;
let nota2 = 0;
let nota3 = 0;
let somanota = nota1 + nota2 + nota3;
let media = somanota/3;
if (media >= 7){
    console.log(`o ${nome} passou de ano`);
} else if ( media >= 5){
    console.log(`o ${nome} ficou de recuperação`);
}else {
    console.log(`o ${nome} reprovou`);
}

// -----------------------------------------------------------------

// 10. Sistema de classificação de produto
// Crie as variáveis produto, preco e estoque. Utilize estruturas if...else if...else para analisar o estoque e o preço do produto. Se o estoque for 0, informe que o produto está esgotado; se for menor ou igual a 3, informe que o estoque está baixo; caso contrário, informe que o estoque está disponível. Além disso, verifique se o preço é superior a R$ 3.000,00 para classificá-lo como produto de alto valor ou, caso contrário, como produto de valor acessível. Ao final, apresente todas as informações utilizando interpolação de strings.

let produto = 'bala';
let preco = 25000;
let estoque = 0;

if (preco >= 3000){
    console.log(`o produto ${produto} custa ${preco} então é de alto valor`);
}else{
    console.log(`o produto ${produto} custa ${preco} então não é de alto valor`);
}

if (estoque >= 4){
    console.log(`o estoque de ${produto} está normal`);
} else if (estoque <= 0){
    console.log(`${produto} acabou`);
}else {
    console.log(`O estoque de ${produto} está acabando`);
}
