from random import shuffle
# Exercício 01
# Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

# Exercício 02
# Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres
# embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer
# outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão
# devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

def exercicio_01():
  num = int(input('Numero: '))
  for t in range(0, 11):
    print(f'{num} x {t} = {num * t}')
    # ou
    # print('\n{} x {} = {}'.format(num, t, (num * t)))

def exercicio_02():
  name = input('Nome: ')

  nameArray = list(name.lower())
  shuffle(nameArray)

  print(''.join(nameArray))

exercicio_01()
exercicio_02()

# 03
def checa_valor(list):
  elem = list[0]
  for a in list:
    if a > elem:
      elem = a
  return elem

print(checa_valor([4, 10, 18, -7])) # 18

# 02
numeros = [10, 20, 30, 40, 50, 60, 70]

print(numeros[2])
print(numeros[1:4])
print(numeros[:2])