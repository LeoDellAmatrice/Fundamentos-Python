coisas = {
    "maracujá": 2.49,
    "banana": 1.29,
    "maçã": 3.49,
    "laranja": 2.19,
    "cenoura": 1.99,
    "batata": 1.79,
    "alface": 2.29,
    "tomate": 3.89,
    "frango": 12.49,
    "carne bovina": 24.99,
    "leite": 3.19,
    "pão": 4.49,
    "arroz": 6.99,
    "feijão": 7.49,
    "açúcar": 3.29,
    "café": 8.99,
    "queijo": 21.49,
    "iogurte": 1.19,
    "manteiga": 5.29,
    "óleo": 4.79
}
valor_total = 0
i = 1
for nome, preco in coisas.items():
    print(f"{i}-{nome} = R${preco}")
    i += 1
while True:
    item_procurado = input("qual o nome do item que deseja comprar? ")

    for item, preco in coisas.items():
        if item == item_procurado:
            print(f'O valor do {item_procurado} é R$ {preco:.2f}')
            valor_total += preco
            print(f"Valor total da compra: {valor_total:.2f}")
            break
    else:
        print(f'O item {item_procurado} não foi encontrado.')





