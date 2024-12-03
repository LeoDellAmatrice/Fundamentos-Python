def contar_caracteres(frase: str) -> int:
    return len(frase)


def contar_caracteres_sem_espaco(frase: str) -> int:
    return len(frase.replace(" ", ""))


def contar_palavras(frase: str) -> int:
    return len(frase.split(" "))


texto = input("digite uma frase para ter a contagem de caracteres: ")
print(f"Sua frase foi: {texto}")
print(f"A quantidade de caracteres é de: {contar_caracteres(texto)}")
print(f"A quantidade de caracteres sem espaco é: {contar_caracteres_sem_espaco(texto)}")
print(f"A quantidade de palavras é de: {contar_palavras(texto)}")
