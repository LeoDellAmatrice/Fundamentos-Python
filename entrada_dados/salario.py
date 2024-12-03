salario_atual = float(input("Digite o valor do seu salario atual: "))
percentual_aumento = float(input("digite a porcentagem de aumento(apenas numero): "))

novo_salario = salario_atual + salario_atual * (percentual_aumento / 100)

print(f"O novo salario, após um aumento de {percentual_aumento}%, é de R$ {novo_salario:.2f}")
