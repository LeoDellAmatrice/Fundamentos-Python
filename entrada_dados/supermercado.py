nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto(apenas numeros): "))

valor_desconto = preco_produto - preco_produto * (desconto / 100)

print(f"o valor do produto {nome_produto} após o desconto de {desconto}% é de {valor_desconto:.2f}")

