def escrever():
    file = open('arquivo.txt', mode='w')

    file.write("nome e idade\n")
    file.write("Beatriz 27\n")
    file.write("Carlos 19\n")

    print("Vincenzo 27", file=file)

    lines = ["Ricardo 33\n", "Ster 45\n"]
    file.writelines(lines)

    file.close()


def ler():
    file = open('arquivo.txt', mode='r')

    content = file.read()
    print(content)

    file.close()


def numero_de_linhas():
    file = open('arquivo.txt', mode='r')
    lines = 0

    for line in file:
        lines += 1

    print(f"O arquivo tem {lines} linhas")


escrever()
ler()
numero_de_linhas()
