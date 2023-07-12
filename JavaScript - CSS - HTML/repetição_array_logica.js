// 01 - Crie uma função usando o operador &&

// JavaScript possui um operador lógico `&&`, o qual recebe dois valores
// e retorna `true` se ambos os valores são verdadeiros, e retorna `false`
// se algum dos valores não o for.

// Considerando isso, implemente na função `compareTrue`, um código que ao
// receber dois parâmetros booleanos deve:

// - Retornar `true` se ambos os valores forem verdadeiros;
// - Retornar `false` se um ou ambos os parâmetros forem falsos.

// Faça a função somente utilizando o operador `&&`.

function compareTrue(valor1, valor2) {
  let absoluto;
  if (valor1 === true && valor2 === true) {
    absoluto = true;
  } else {
    absoluto = false;
  }
  return absoluto;
}

// 2 - Crie uma função que calcule a área de um triângulo

// Escreva uma função com o nome `calcArea` que receba um valor de base
// (chamado `base`) e outro de altura (chamado `height`) de um triângulo
// e retorne o cálculo da sua área.

// Lembre-se que a área de um triângulo é calculada através da seguinte
// fórmula: (base * altura) / 2.

function calcArea(base, height) {
  let calculo = (base * height) / 2;
  return calculo;
}

// 3 - Crie uma função que divida a frase

// Escreva uma função com o nome `splitSentence`, a qual receberá
// uma string e retornará uma array de strings separadas por cada
// espaço na string original.

// Exemplo: se a função receber a string `"go Trybe"`, o retorno
// deverá ser `['go', 'Trybe']`.

function splitSentence(frase) {
  let palavra = frase.split(" ");
  return palavra;
}

// 4 - Crie uma função que use concatenação de strings

// Escreva uma função com o nome `concatName` que, ao receber uma
// array de strings, retorne uma string com o formato `'ÚLTIMO ITEM, PRIMEIRO ITEM'`,
// independente do tamanho da array.

// Isso quer dizer que, caso o parâmetro passado para `concatName` seja a Array
// ['Lucas', 'Cassiano', 'Ferraz', 'Paolillo'], a função deverá retornar `Paolillo, Lucas`.

function concatName(nomes) {
  let nome = [];
  nome.push(nomes[nomes.length - 1]); // Ultimo Item
  nome.push(nomes[0]); // Primeiro item
  let nomeForm = nome.join(", "); // Juntanto
  return nomeForm;
}

// 5 - Crie uma função que calcule a quantidade de pontos no futebol

// Escreva uma função com o nome `footballPoints` que receba o número de
// vitórias (esse parâmetro deverá se chamar `wins`) e o número de
// empates (esse parâmetro deverá se chamar `ties`) e retorne a quantidade
// de pontos que o time marcou em um campeonato.

// Para tanto, considere que cada vitória vale 3 pontos e cada empate vale 1 ponto.

function footballPoints(wins, ties) {
  let winsPoint = (tiesPoint = 0);
  for (let iw = 1; iw <= wins; iw++) {
    winsPoint += 3;
  }
  for (let it = 1; it <= ties; it++) {
    tiesPoint++;
  }
  let total = winsPoint + tiesPoint;
  return total;
}

// 6 - Crie uma função que calcule a repetição do maior número

// Escreva uma função chamada `highestCount` que, ao receber uma array de
// números, retorne a quantidade de vezes que o maior deles se repete.

// Exemplo: caso o parâmetro de `highestCount` seja uma array com valores
// `[9, 1, 2, 3, 9, 5, 7]`, a função deverá retornar `2`, que é a quantidade
// de vezes que o número `9` (maior número do array) se repete.

function highestCount(sequencia) {
  let numComp = sequencia[0];
  // Achar o Maior:
  for (let times = 0; times <= sequencia.length - 1; times++) {
    if (sequencia[times] >= numComp) {
      numComp = sequencia[times];
    }
  }
  // Qtas vezes tem o maior:
  let point = 0;
  for (let times = 0; times <= sequencia.length - 1; times++) {
    if (numComp === sequencia[times]) {
      point++;
    }
  }
  return point;
}

// 7 - Crie uma função de Caça ao Rato

// Imagine que existem dois gatos, os quais chamaremos de `cat1` e `cat2`,
// e que ambos estão caçando um mesmo rato chamado `mouse`. Imagine que os
// animais estão em uma reta, cada um em uma posição representada por um número.

// Sabendo disso, crie uma função chamada `catAndMouse` que, ao receber a posição
// de `mouse`, `cat1` e `cat2`, **nessa ordem**, calcule as distâncias entre o
// rato e cada um dos gatos, em seguida, retorne qual dos felinos irá alcançar
// o rato primeiro (aquele que estiver mais perto do rato).

// Exemplo: caso o gato `cat2` esteja a 2 unidades de distância do rato, e `cat1`
// esteja a 3 unidades, sua função deverá retornar `"cat2"`.

// Caso os gatos estejam na mesma distância do rato, a função deverá retornar a
// string `"os gatos trombam e o rato foge"`.

function catAndMouse(mouse, cat1, cat2) {
  let mouseCat1 = Math.abs(cat1 - mouse);
  let mouseCat2 = Math.abs(cat2 - mouse);
  if (mouseCat1 > mouseCat2) {
    return "cat2";
  } else if (mouseCat1 < mouseCat2) {
    return "cat1";
  } else {
    return "os gatos trombam e o rato foge";
  }
}

// 8 - Crie uma função FizzBuzz

// Crie uma função chamada `fizzBuzz` que receba uma array de números e retorne
// uma array da seguinte forma:

// - Para cada número do Array que seja divisível apenas por 3, apresente uma string `"fizz"`;
// - Para cada número do Array que seja divisível apenas por 5, apresente uma string `"buzz"`;
// - Caso o número seja divisível por 3 e 5, retorne a string `"fizzBuzz"`;
// - Caso o número não possa ser dividido por 3 nem por 5, retorne a string `"bug!"`;

function fizzBuzz(numArray) {
  let resposta = [];
  for (let num = 0; num <= numArray.length - 1; num++) {
    if (numArray[num] % 3 == 0) {
      if (numArray[num] % 5 == 0) {
        resposta.push("fizzBuzz");
      } else {
        resposta.push("fizz");
      }
    } else if (numArray[num] % 5 == 0) {
      resposta.push("buzz");
    } else {
      resposta.push("bug!");
    }
  }
  return resposta;
}

// 9 - Crie uma função que Codifique e Decodifique

// Crie duas funções: a primeira deverá se chamar `encode` e, ao receber uma
// string como parâmetro, deverá trocar todas as vogais minúsculas por números,
// de acordo com o formato a seguir:

// a -> 1 \
// e -> 2 \
// i -> 3 \
// o -> 4 \
// u -> 5

// Ou seja, caso o parâmetro de `encode` seja `"hi there!"`, o retorno deverá
// ser `"h3 th2r2!"`.

// A segunda função deverá se chamar `decode` e faz o contrário de `encode` - ou
// seja, recebe uma string contendo números no lugar de letras minúsculas e retornará
// uma string com vogais minúsculas no lugar dos números (então, caso o parâmetro de
// `decode` seja `"h3 th2r2!"`, o retorno deverá ser `"hi there!"`).

function encode(frase) {
  return frase
    .replace(/a/g, "1")
    .replace(/e/g, "2")
    .replace(/i/g, "3")
    .replace(/o/g, "4")
    .replace(/u/g, "5");
}
function decode(frase) {
  return frase
    .replace(/1/g, "a")
    .replace(/2/g, "e")
    .replace(/3/g, "i")
    .replace(/4/g, "o")
    .replace(/5/g, "u");
}

// 10 - Crie uma função de Lista de Tecnologias

// Crie uma função que recebe um array de nomes de tecnologias que você quer aprender.
// Essa função deve receber também um segundo parâmetro chamado `name` com um nome.

// Para cada tecnologia no array, crie um objeto com a seguinte estrutura:

// {
//   tech: "NomeTech",
//   name: name
// }

// Estes objetos devem ser inseridos em uma nova lista em ordem crescente a partir do
// campo `tech` no objeto.
// A saída da sua função deve ser uma lista de objetos ordenada pelo campo `tech` dos
// objetos com o formato acima.

function techList(technologies, name) {
  let array10 = [];
  if (technologies.length === 0) {
    return "Vazio!";
  } else {
    for (let tech of technologies.sort()) {
      array10.push({ tech, name });
    }
  }
  return array10;
}

// 11 - Crie uma função de Número de Telefone

// Crie uma função chamada `generatePhoneNumber` que receba uma array com 11 números e
// retorne um número de telefone, respeitando parênteses, traços e espaços.

// Exemplo: caso o parâmetro da função seja [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1],
// `generatePhoneNumber` deverá retornar `(12) 34567-8901`.

// - Se a função receber um array com tamanho diferente de 11, a mesma deve retornar
// `"Array com tamanho incorreto."`.

// - Caso algum dos números da array seja menor que 0, maior que 9 ou se repita 3 vezes
// ou mais, `generatePhoneNumber` deverá retornar a string `"não é possível gerar um
// número de telefone com esses valores"`.

function generatePhoneNumber(tel) {
  if (tel.length == 11) {
    for (let index1 = 0; index1 < 11; index1++) {
      let point = 0;
      for (index2 = 0; index2 < 11; index2++) {
        if (tel[index1] === tel[index2]) {
          point++;
          if (point === 3) {
            return "não é possível gerar um número de telefone com esses valores";
          }
        }
      }
      if (tel[index1] < 0 || tel[index1] > 9) {
        return "não é possível gerar um número de telefone com esses valores";
      }
    }
    return `(${tel[0]}${tel[1]}) ${tel[2]}${tel[3]}${tel[4]}${tel[5]}${tel[6]}-${tel[7]}${tel[8]}${tel[9]}${tel[10]}`;
  } else {
    return "Array com tamanho incorreto.";
  }
}

// ### 12 - Crie uma função de Condição de existência de um triângulo

// Um triângulo é composto de três linhas: `lineA`, `lineB` e `lineC`. Crie uma
// função chamada `triangleCheck` que deverá receber as três linhas como parâmetro
// e retornar se é possível formar um triângulo com os valores apresentados de cada linha.

function triangleCheck(lineA, lineB, lineC) {
  if (
    Math.abs(lineA + lineB > lineC) &&
    Math.abs(lineB + lineC > lineA) &&
    Math.abs(lineC + lineA > lineB)
  ) {
    return true;
  } else {
    return false;
  }
}

// Desafio 13
function hydrate(frase) {
  let alcolismo = frase.match(/\d+/g);
  let consiencia = 0;
  for (let index = 0; index < alcolismo.length; index++) {
    consiencia += Number.parseInt(alcolismo[index]);
  }
  if (consiencia == 0 || consiencia > 1) {
    return `${consiencia} copos de água`;
  } else {
    return `${consiencia} copo de água`;
  }
}

// ***********************DESAFIO 13****************************

let frase =
  "Meu nome é Vincenzo eu tenho 28 anos, 1,87 cm de altura e nasci dia 28 de agosto de 1995";
/*
Usando RegEx \d Metacharacter:
'/d' progura por digitos
'match()'
*/
console.log(frase.match(/\d/g));
console.log(frase.match(/\d+/g)); // g de global... para agrupar
console.log("------------------------------------------------------");
/*
Usando RegEx \D Metacharacter:

*/
console.log(frase.replace(/\D/g, "")); // g faz uma pesquisa global, sem o 'g' retorna a string normal
