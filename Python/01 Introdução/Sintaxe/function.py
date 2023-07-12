def analyze(text: str) -> str:
    report = ''
    count_words = len(text.split(' '))
    report += f"Numero de palavras: {count_words}\n"

    char_counter = dict()
    for char in text:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    report += f"Ocorrencias por caractere: {char_counter}"

    return report


text_to_analyze = (
    "estou escrevendo este texto para poder testar a funcao acima")

print(analyze(text_to_analyze))
