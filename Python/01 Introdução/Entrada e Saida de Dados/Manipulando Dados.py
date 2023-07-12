from random import randint  # ou import random
from sys import argv, stderr


def input_test() -> str:
    # O programa permanece parado até que uma mensagem seja digitada
    res = input('Digite uma mensagem: ')
    print(f'voce digitou: {res}')


def random_number() -> str:
    guess = ''
    a_number = randint(1, 10)

    while (guess != a_number):
        guess = int(input('Qual o numero sorteado? '))

    print(f'Finalmente!!! o numero era {a_number}')


def passando_parametros() -> str:
    if __name__ == "__main__":
        for argument in argv:
            print("Recebendo o argumento => ", argument)


def arquivo_nao_encontrado() -> str:
    err_msg = 'Arquivo nao encontrado.'
    print(f"Erro: {err_msg}", file=stderr)


def interpolacao(x, y):
    print(f"{x} / {y} = {x / y:.2f}")
    print(f"{x:.^3}")


# input_test()
# random_number()
# passando_parametros() # python3 Exemplo.py test 1 2 param
# arquivo_nao_encontrado()
# interpolacao(2, 6)


# Exercicios


def exercicio_01():
    name = input('Qual o seu nome? ')
    for letter in name:
        print(letter)


def exercicio_02():
    numberInput = input('Insira valores aqui, separados por espaço: ')
    numbers = numberInput.split(" ")
    counter = 0

    for number in numbers:
        if not number.isdigit():
            print("Erro ao somar valores... colo um numero valido")
            return
        else:
            counter += int(number)

    print(f"O resultado da soma é {counter}")


# exercicio_01()
# exercicio_02()
