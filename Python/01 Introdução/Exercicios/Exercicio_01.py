# Exercicio 01
from random import sample
from unittest import result

def busca_linear(param_01, param_02):
    for item in param_01:
        if param_02 == item:
            return True

    return False


lista = sample(range(100), 25)

print(sorted(lista))

print(busca_linear(lista, 10))

# Exercicio 02
vogais = 'aeiou'

resultado = vogais.index('o')

print(resultado)

# Exercicio 03
def busca_binaria(param_01, param_02):
    min = 0
    max = len(param_01) - 1

    while min <= max:
        middle = (min + max) // 2
        if param_02 < param_01[middle]:
            max = middle - 1
        elif param_02 > param_01[middle]:
            min = middle + 1
        else:
            return True
    return False


list = list(range(1, 50))

print(list)
print(busca_binaria(list, 10))
