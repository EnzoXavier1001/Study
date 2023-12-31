frase = 'curso em Vídeo Python'
print('--- FATIAMENTO ----')
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[15:])
print(frase[9::3])

print('--- ANÁLISE ----')
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('curso' in frase)

print('--- TRANSFORMAÇÃO ----')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print('--- DIVISAO ----')
print(frase.split)

print('--- JUNÇÃO ----')
print('-'.join(frase))