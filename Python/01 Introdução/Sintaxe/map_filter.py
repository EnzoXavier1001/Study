# map() => função + objeto
linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'C++']

nova_lista = map(lambda x: x.lower(), linguagens)
print(f'Nova lista 1.0: {nova_lista}\n')

nova_lista = list(nova_lista)
print(f'Nova lista 1.2: {nova_lista}\n')

# filter()
numeros = list(range(0, 21)) # cria uma lista de 0 a 20

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_impares = list(filter(lambda x: x % 2 == 1, numeros))

print('Pares: ', numeros_pares)
print('Impares: ', numeros_impares)