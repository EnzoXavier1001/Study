# Exercicio 01
# Crie uma função que receba dois números e retorne o maior deles.

def exercicio_01(num01, num02):
    if num01 > num02:
        return num01
    return num02

# Exercicio 02
# Calcule a média aritmética de valores contidos em uma lista.

def exercicio_02(list):
    sum = 0
    for num in list:
        sum += num
    return sum/len(list)

# Exercicio 03
# Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.

def exercicio_03_1(n):
    width = n * '*'
    for t in width:
        print(width)

def exercicio_03_2(n):
    for row in range(n):
        print(n * '*')

# Exercicio 04
# Crie uma função que receba uma lista de nomes e retorne o nome com a
# maior quantidade de caracteres. Por exemplo, para:
#     ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
# o retorno deve ser "Fernanda".

def exercicio_04(names):
    bigger_name = names[0]
    for name in names:
        if len(name) > len(bigger_name):
            bigger_name = name
    return bigger_name

# Exercicio 05
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que
# retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem
# compradas e o preço total a partir do tamanho de uma parede (em m²).

def exercico_05():
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price

# Exercicio 06
# Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo
# formado ou "não é triangulo", caso não seja possível formar um triângulo.

def exercicio_06(side1, side2, side3):
    is_triangle = (
            side1 + side2 > side3 and
            side2 + side3 > side1 and
            side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"


