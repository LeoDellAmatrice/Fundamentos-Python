def contar_vogais(text: str):
    vogais = "aeiouáéíóúãõ"
    soma = 0
    for char in text:
        if char.lower() in vogais:
            soma += 1
    return soma


palavra = input("digite a palavra que deseja saber quantas vogais possui: ")
print(F"a palavra {palavra} possui {contar_vogais(palavra)} vogais")
