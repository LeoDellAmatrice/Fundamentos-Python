import random


def gerar_pix(nome: str, cpf: str) -> str:
    if not validar_cpf(cpf):
        return "CPF inválido!"
    if not validar_nome(nome):
        return "Nome muito curto para criar uma chave Pix"
    digitos = remover_repetidos_espaco(cpf) + remover_repetidos_espaco(nome)
    digitos = embaralhar_string(digitos).replace(" ", "")
    pix = ""
    for i in range(0, 16):
        pix += str(digitos[i])
        if i in [3, 7, 11]:
            pix += "-"
    return pix


def embaralhar_string(s):
    lista_caracteres = list(s)  # Converte a string em uma lista de caracteres
    random.shuffle(lista_caracteres)  # Embaralha a lista
    return ''.join(lista_caracteres)


def validar_cpf(cpf: str) -> bool:
    if len(cpf) == 11:
        return True
    return False


def validar_nome(nome: str) -> bool:
    if len(nome) >= 13:
        return True
    return False


def remover_repetidos_espaco(texto: str) -> str:
    resultado = ""
    for letra in texto:
        if letra not in resultado:
            resultado += letra
    return resultado.strip()


nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF(apenas numeros): ")
print(gerar_pix(nome, cpf))
