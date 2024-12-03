def inverter(string: str) -> str:
    return string[::-1]


def contar_vogais(string: str) -> int:
    vogais = "aeiouáéíóúãõ"
    soma = 0
    for char in string:
        if char.lower() in vogais:
            soma += 1
    return soma


texto = input("Digite um texto para ser invertido: ")
print(f"texto invertido: {inverter(texto)}")
print(f"o texto possui {contar_vogais(texto)} vogais.")
