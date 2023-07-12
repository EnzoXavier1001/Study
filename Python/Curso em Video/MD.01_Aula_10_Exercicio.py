    #Exercício 01
# from random import randint
# num = int(input('Digite o número: '))
# r = randint(0, 5)
# if num == r:
#     print('Parabens você ganhou da máquina!')
# else:
#     print('A máquina ganho de voce... o número correto era {}.'.format(r))

    #Exercício 02
# vel = float(input('Digite a velocidade do carro em Km/h: '))
# if vel > 80:
#     multa = 7 * (vel - 80)
#     print('Você foi multado, a multa sera de R$ {:.2f}'.format(multa))
# else:
#     print('Você não foi multado... ufa!!')

    #Exercício 03
# num = int(input('Digite o número: '))
# if num % 2 == 0:
#     print('Número é par.')
# else:
#     print ('Número impar')

#Exercício 04
# trip = float(input('Qual a distância da viajem em Km: '))
# if trip >= 200:
#     tax = 0.45 * trip
#     print('Sua viagem custará R$ {}'.format(tax))
# else:
#     tax = 0.5 * trip
#     print('Sua Viagem custará R$ {}'.format(tax))

    #Exercício 05
# ano = int(input('Ano a análisar: '))
# if ano % 4 == 0:
#     print('Por o ano {}, é bissexto.'.format(dias))
# else:
#     print('Por o ano {}, não é bissexto.'.format(dias))

    #Exercício 06
# n1 = float(input('Primeiro Número:'))
# n2 = float(input('Segundo Número:'))
# n3 = float(input('Terceiro Número:'))
# if n1 != n2 != n3:
#     if n1 > n2 and n1 > n3:
#         print('{:.2f} é o maior número.'.format(n1))
#     if n2 > n1 and n2 > n3:
#         print('{:.2f} é o maior número.'.format(n2))
#     if n3 > n1 and n3 > n2:
#         print('{:.2f} é o maior número.'.format(n3))
#     if n1 < n2 and n1 < n3:
#         print('{:.2f} é o menor número.'.format(n1))
#     if n2 < n1 and n2 < n3:
#         print('{:.2f} é o menor número.'.format(n2))
#     if n3 < n1 and n3 < n2:
#         print('{:.2f} é o menor número.'.format(n3))
# else:
#     print('Números iguais.')

    #Exercício 07
# salar = float(input('Digite seu salário atual: '))
# if salar <= 1250:
#     aumento = salar + (salar * 0.015)
#     print('Seu novo salário será de R$ {:.2f}'.format(aumento))
# else:
#     aumento = salar + (salar * 0.010)
#     print('Seu novo salário será de R$ {:.2f}'.format(aumento))

    #Exercício 08
# n1 = float(input('Digite o primeiro lado do triangulo: '))
# n2 = float(input('Digite o segundo lado do triangulo: '))
# n3 = float(input('Digite o terceiro lado do triangulo: '))
# if n1 + n2 >= n3 and n2 + n3 >= n1 and n3 + n1 >= n2:
#     print('O triângilo pode existir.')
# else:
#     print('O triângilo não pode existir.')