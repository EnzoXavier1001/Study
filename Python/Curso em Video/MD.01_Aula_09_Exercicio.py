    #Exercicio 01
# nome = str(input('Seu nome completo: '))
# nome1 = nome.upper()
# nome2 = nome.lower()
# nome3 = nome.strip() #depois jogar na função len(nome3) - name3.count(' ')
# nome4 = nome.split() #pegar o primeiro nome no len()
# print('Com letra Maiúscula: {}.\nCom letra Minúscula: {}.'.format(nome1, nome2))
# print('Seu nome tem {} letras'.format(len(nome3) - nome3.count(' ')))
# print('O primeiro nome tem {} letras'.format(len(nome4[0])))

    #Exercicio 02
# num = int(input('Digite um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))

    #Exercicio 
# cidade = str(input('Nome da Cidade:')).strip()
# print(cidade[:5].upper() == 'SANTO')

    #Exercicio 04
# nome = str(input('Qual seu Nome:')).strip()
# print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

    #Exercicio 05
# frase = str(input('Digite a Frase: ')).strip().upper()
# print('A frase tem {} letras "a"'.format(frase.count('A')))
# print('Aparecendo na posição {} na primeira vez.'.format(frase.find('A')))
# print('Aparecendo na posição {} na segunda vez.'.format(frase.rfind('A')))

    #Exercicio 06
# nome = str(input('Digite seu nome:')).strip().split()
# print('Primeiro nome: {}.'.format(nome[0]))
# print('Ultimo nome: {}.'.format(nome[len(nome) - 1]))