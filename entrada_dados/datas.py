ano_nascimento = int(input("digite o seu ano de nascimento: "))

ano_atual = 2024

idade_anos = ano_atual - ano_nascimento
idade_mes = idade_anos * 12
idade_dias = idade_mes * 30

print(f"você possui {idade_anos} anos de idade, {idade_mes} meses de idade ou {idade_dias} dias de idade")
