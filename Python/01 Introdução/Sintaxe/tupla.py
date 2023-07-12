vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto: {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Prosição: {p} | valor: {x}")

# Desempacotamento de Tupla
city, uf, year, pop = ('Presidente Prudente', 'SP', 2020, 23_371)
