def try_to_open_a_file():
    try:
        file = open('arquivo.txt', mode='r')
    except OSError as err:
        print('Arquivo não existe')
    else:
        print('Arquivo encontrado com sucesso')
        file.close()
    finally:
        print('Tentativa de abrir o arquivo')


try_to_open_a_file()
