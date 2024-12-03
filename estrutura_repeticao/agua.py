qnt_pessoa = int(input("Quantas pessoas moram na sua casa?"))
agua = 0

for i in range(qnt_pessoa):
    idade = float(input(f"Qual a idade da {i+1} pessoa? "))

    if idade <= 10:
        agua += 18
    elif idade <= 18:
        agua += 30
    elif idade <= 25:
        agua += 42
    elif 150 > idade > 25:
        agua += 24
    else:
        print("idade invalida")

print(f"o total de litros de agua gastos é de {agua}")
valor = agua * 0.60
print(f"o total de gastos com água na casa é de R$ {valor:.2f}")
