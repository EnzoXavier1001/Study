def imprimir_parametro(**params):
  print(f"\nTipo de objeto recebido: {type(params)}")

  qtd_param = len(params)
  print(f"Quantidades de paramentros: {qtd_param}\n")
  
  for param, valor in params.items():
    print(f"variavel: {param} | valor: {valor}")
  
  print("")

imprimir_parametro(cidade = "Santos", nome = "Vincenzo", idade = 26);