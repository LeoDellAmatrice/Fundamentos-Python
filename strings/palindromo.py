def palindromo(text: str) -> bool:
    if text == text[::-1]:
        return True
    else:
        return False


texto = input("digite uma palavra para verificar se é palindromo: ")
if palindromo(texto):
    print(f"{texto} é um palindromo")
else:
    print(f"{texto} não é um palindromo")
    print(f"A inversão é {texto[::-1]}")
