texto = "Um texto qualquer para usar de exemplo"

print(f"Tamanho do texto: {len(texto)}")                      # 38
print(f"'exemplo' in text: {'exemplo' in texto}")             # true
print(f"Quantidade de 'e' in texto: {texto.count('e')}")      # 5
print(f"As 5 primeiras letras: {texto[0:6]}")                 # Um tex

# Usando split()
palavras = texto.split()
print(f"Palavras: {palavras}") 
print(f"Tamanho de 'palavras': {len(palavras)}")

# Criando Arrays
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
  print(f'Prosição: {vogais.index(vogal)} | valor: {vogal}')

# List Comprehension (listcomp)
linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'C++']

print('Antes da listcomp: ', linguagens)

linguagens = [item.lower() for item in linguagens]

print('Depois da listcomp: ', linguagens)