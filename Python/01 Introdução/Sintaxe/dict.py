# Como se fosse um objeto em JavaScript

# Exemplo 01
obj_01 = {}
obj_01['nome'] = 'Vincenzo'
obj_01['idade'] = 27

# Exemplo 02
obj_02 = {
    'nome': 'Vincenzo',
    'idade': 27
}

# Exemplo 03 => Criando com tuplas
obj_03 = dict([('nome', 'Vincenzo'), ('idade', 27)])

# Exemplo 04 => Com a função built-in zip()
obj_04 = dict(zip(['nome', 'idade'], ['Vincenzo', 27]))

print(obj_01 == obj_02 == obj_03 == obj_04)
