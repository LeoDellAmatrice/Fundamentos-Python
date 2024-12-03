itens = [
    {
        "nome": "McDonald's",
        "cozinha": "fast-food",
        "endereco": "Rua da Paz, 123",
        "avaliacao": "4.0",
        "especialidade": "lanche",
        "prato_principal": [['Big Mac', 20], ['Cheeseburger', 15], ['McNuggets', 18]],
        "bebida": [['Coca-Cola', 5], ['Fanta', 5], ['Suco de laranja', 6]],
        "sobremesa": [['Sundae', 4], ['McFlurry', 6]],
        "horario_funcionamento": "10h às 22h",
        "formas_pagamento": ["Dinheiro", "Cartão", "Pix"]
    },
    {
        "nome": "Restaurante Italiano Bella Italia",
        "cozinha": "italiana",
        "endereco": "Avenida dos Estados, 456",
        "avaliacao": "4.5",
        "especialidade": "massa",
        "prato_principal": [['Macarrão à bolonhesa', 35], ['Pizza Margherita', 40], ['Lasanha', 38]],
        "bebida": [['Vinho tinto', 25], ['Vinho branco', 25], ['Água com gás', 4]],
        "sobremesa": [['Tiramisu', 10], ['Panna cotta', 8]],
        "horario_funcionamento": "12h às 15h e 19h às 23h",
        "formas_pagamento": ["Cartão", "Pix"]
    },
    # ... adicione mais restaurantes aqui
]

pedidos = []


def mostrar_restaurante(index: int, categoria: str = None) -> [None, str]:
    if not categoria:
        print(f"nome: {itens[index]['nome']}")
        print(f"estilo: {itens[index]['cozinha']}")
        print(f"endereço: {itens[index]['endereco']}")
        print(f"avaliação: {itens[index]['avaliacao']}")
        print(f"Especialidade: {itens[index]['especialidade']}")
        print(f"formas pagamento: {itens[index]['formas_pagamento']}")
        print(f"Horario de funcionamento: {itens[index]['horario_funcionamento']}")
    else:
        return itens[index][categoria]
    return


def escolher_restaurante() -> int:
    for restaurante in range(0, len(itens)):
        print('==== ==== ==== ====')
        print(f'Opção {restaurante + 1} de restaurantes: ')
        mostrar_restaurante(restaurante)

    print('==== ==== ==== ====')
    escolha = int(input('Digite o numero do restaurante que deseja pedir: ')) - 1

    return escolha


def restaurante_escolhido(index: int) -> None:
    print('==== ==== ==== ====')
    print(f"O restaurante escolhido foi: {mostrar_restaurante(index, 'nome')}")


def escolher_estilo(index: int) -> int:
    print('==== ==== ==== ====')
    print("escolha o que desejar: ")
    return int(
        input("1 - Pratos principais \n2 - Bebidas \n3 - Sobremesa \n4 - ver carrinho\n5 - Sair/Finalizar \nEscolha:"))


def nome_pedido(index: int, categoria: str, pedido: int) -> str:
    return itens[index][categoria][pedido][0]


def escolher_principal(index: int) -> None:
    numero = int(input("Digite o numero do item que deseja: ")) - 1
    print(f"produto {nome_pedido(index, 'prato_principal', numero)} adiconado ao carrinho.")
    for i in range(len(pedidos)):
        if pedidos[i]['nome'] == mostrar_restaurante(index, 'nome'):
            pedidos[i]['prato_principal'].append(numero)
            return
    restaurante = {
        'nome': mostrar_restaurante(index, 'nome'),
        'prato_principal': [numero]
    }
    pedidos.append(restaurante)


def mostrar_pratos_principal(index: int) -> None:
    print('==== ==== ==== ====')
    print("Pratos Principais:")
    for i, prato in enumerate(itens[index]['prato_principal']):
        nome = prato[0]
        preco = prato[1]
        print(f"{i + 1} - {nome}: R${preco:.2f}")
    return


""" 
def mostrar_pedido(index: int, categoria: str) -> None:
    return pedidos[index][categoria][0]
"""


# def ver_carrinho():
#    print('==== ==== ==== ====')
#    for i in range(len(pedidos)):
#        print(f'{i+1} - {mostrar_pedido(i,)}')


def main():
    restaurante = escolher_restaurante()
    restaurante_escolhido(restaurante)
    while escolha < 5:
        escolha = escolher_estilo(restaurante)
        if escolha == 1:
            mostrar_pratos_principal(restaurante)
            escolher_principal(restaurante)
        elif escolha == 4:
            ver_carrinho()
    print(pedidos)


if __name__ == '__main__':
    main()
