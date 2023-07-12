import re

lista = [10, 4, 1, 15, -3]

lista_sorted_01 = sorted(lista)
lista_sorted_02 = lista.sort()

print(lista)
print('Lista 01: ', lista_sorted_01)
print('Lista 02: ', lista_sorted_02)

# Com atribuições multiplas
list = [5, -1]

if list[0] > list[1]:
  list[0], list[1] = list[1], list[0]

print(list)

# Forma manual de execultar o sort
def selection_sort(param):
  n = len(param)

  for i in range(0, n):
    index_menor = i

    for j in range(i + 1, n):
      if param[j] < param[index_menor]:
        index_menor = j

    param[i], param[index_menor] = param[i], param[index_menor]

  return param

print(selection_sort([10, 9, 5, 8, 11, -1, 3]))

# Bubble sort
def bubble_sort(param):
  n = len(param)

  for i in range(n - 1):
    for j in range(n - 1):
      if param[j] > param[j + 1]:
        param[j], param[j + 1] = param[j + 1], param[j]
  
  return param

print(bubble_sort([10, 9, 5, 8, 11, -1, 3]))

# Insertion sort
def insertion_sort(param):
  n = len(param)

  for i in range(1, n):
    valor_inserido = param[i]
    j = i - 1

    while j >= 0 and param[i] > valor_inserido:
      param[j + 1] = param[j]
      j -= 1
    param[j + 1] = valor_inserido

  return param

print(insertion_sort([10, 9, 5, 8, 11, -1, 3]))

# Merge sort
def merge_sort(list):
  if len(lista) <= 1: return list
  else:
    meio = len(lista)
    esquerda = merge_sort(list[:meio])
    direita = merge_sort(list[meio:])
    return executar_merge(esquerda, direita)

def executar_merge(esquerda, direita):
  sub_lista_ordenada = []
  topo_esquerda, topo_direita = 0, 0
  while topo_esquerda < len(esquerda) and topo_direita < len(direita):
    if esquerda[topo_direita] <= direita[topo_direita]:
      sub_lista_ordenada.append(esquerda[topo_direita])
      topo_esquerda += 1
    else:
      sub_lista_ordenada.append(direita[topo_direita])
      topo_direita += 1
  sub_lista_ordenada += esquerda[topo_esquerda:]
  sub_lista_ordenada += direita[topo_direita:]
  return sub_lista_ordenada