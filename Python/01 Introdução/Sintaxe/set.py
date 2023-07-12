# Sem uso do construtor
vogais_1 = {'aeiou'}
print(type(vogais_1), vogais_1)

# Com o construtor
vogais_2 = set('aeiouu')
print(type(vogais_2), vogais_2)

# Construtor com lista
vogais_3 = set(['a', 'e', 'i', 'o', 'u'])
print(type(vogais_3), vogais_3)

# Construtor com tupla
vogais_4 = set(('a', 'e', 'i', 'o', 'u'))
print(type(vogais_4), vogais_4)

print(set('uma string'))