import time
carrinho = 0
seila_tambem_nao_sei_tambem = True

def descontos(cupom):
    global carrinho

    if cupom.upper() == "ABC5F":
        return carrinho - (carrinho * 0.05)
    elif cupom.upper() == "DEF10G":
        return carrinho - (carrinho * 0.10)
    elif cupom.upper() == "GHI15J":
        return carrinho - (carrinho * 0.15)
    elif cupom.upper() == "KLM20N":
        return carrinho - (carrinho * 0.20)

    return "Cupom invalido"

def menu_lanches():
    global carrinho
    lista_lanches = {
        "BigMac": 29.90,
        "McChicken": 27.90,
        "Quarteirão Com Queijo": 39.90,
        "McFiesta": 19.90,
        "Chicken Jr": 29.90
    }

    for itens, valor in lista_lanches.items():
        print(f"{itens}: R${valor}")

    escolha_lanche = input("Digite o nome lanche selecionado 🍔: ")
    for itens, valor in lista_lanches.items():
        if escolha_lanche.lower() == itens.lower():
            carrinho += valor
    print(f"O valor total da sua compra é: R${carrinho:.2f}🛒")


def menu_combos():
    global carrinho
    lista_combos = {
        "McLanche Feliz": 28.90,
        "Family box para 2": 30.90,
        "family box para 3": 39.90,
        "Méqui Box Clássico para 3": 39.90,
        "Méqui Box Clássico para 4": 43.90
    }

    for itens, valor in lista_combos.items():
        print(f"{itens}: R${valor}")

    escolha_combo = input("Digite o nome combo selecionado 🍱: ")
    for itens, valor in lista_combos.items():
        if escolha_combo.lower() == itens.lower():
            carrinho += valor
    print(f"O valor total da sua compra é: R${carrinho:.2f}🛒")


def menu_sobremesas():
    global carrinho
    lista_sobremesas = {
        "Mcshake": 14.99,
        "casquinha baunilha": 4.99,
        "casquinha chocolate": 4.99,
        "sundae morango": 9.99,
        "sundae chocolate": 9.99,
        "Top sundae chocolate": 13.99,
        "Top sundae morango": 13.99,
    }

    for itens, valor in lista_sobremesas.items():
        print(f"{itens}: R${valor}")

    escolha_sobremesa = input("Digite o nome da sobremesa que deseja 🍨: ")

    for itens, valor in lista_sobremesas.items():
        if escolha_sobremesa.lower() == itens.lower():
            carrinho += valor
    print(f"O valor total da sua compra é: R${carrinho:.2f}🛒")

def menu_bebidas():
    global carrinho
    lista_bebidas = {
        "Coca-Cola 500ml": 11.90,
        "Coca-Cola 300ml": 9.90,
        "Coca-Cola sem açúcar 500ml": 9.90,
        "Coca-Cola sem açúcar 300ml": 7.50,
        "Fanta Guaraná 500ml": 10.90,
        "Fanta Guaraná 300ml": 8.90,
        "Fanta Laranja 500ml": 10.90,
        "Fanta Laranja 300ml": 8.90,
        "Suco Del Vale Uva 500ml": 8.90,
        "Suco Del Vale Uva 300ml": 6.90,
        "Suco Del Vale Laranja 500ml": 8.90,
        "Suco Del Vale Laranja 300ml": 6.90,
        "Sprite 500ml": 10.90,
        "Sprite 300ml": 9.90,
        "Água 500ml": 1.90,
        "Água 300ml": 0.90
    }

    for itens, valor in lista_bebidas.items():
        print(f"{itens}: R${valor}")

    escolha_lanche = input("Digite o nome da bebida selecionada 🥤: ")
    for itens, valor in lista_bebidas.items():
        if escolha_lanche.lower() == itens.lower():
            carrinho += valor
    print(f"O valor total da sua compra é: R${carrinho:.2f}🛒")


def menu(nome):
    while seila_tambem_nao_sei_tambem == True:
        decisao = input(f"{nome}, você deseja escolher Lanches, Sobremesas, Bebidas ou Combos? 🍔🍨🥤🍱")

        while decisao.lower() not in ["lanches", "lanche", "sobremesas", "sobremesa", "bebidas", "bebida", "combos", "combo"]:
            print("❌Opção inválida! Tente novamente.❌")
            decisao = input(f"{nome}, você deseja escolher Lanches, Sobremesas, Bebidas ou Combos? 🍔🍨🥤🍱")

        if decisao.lower() in ["lanches", "lanche"]:
            menu_lanches()
        elif decisao.lower() in ["sobremesas", "sobremesa"]:
            menu_sobremesas()
        elif decisao.lower() in ["bebidas", "bebida"]:
            menu_bebidas()
        elif decisao.lower() in ["combos", "combo"]:
            menu_combos()
        final = input("Você deseja fazer outra compra? 💵 S/N 💵: ")
        if final.lower() == "s":
            continue
        elif final.lower() == "n":
            pergunta = input("Você tem algum cupom para finalizar a compra? 🎟️ S/N 🎟️: ")
            if pergunta.lower() == "s":
                cupom = input("Digite o codigo do cupom 🎟️: ")
                if descontos(cupom) == "Cupom invalido":
                    print("❌Cupom inválido! Tente novamente.❌")
                else:
                    print(f"O valor final da compra com o desconto foi de: R${descontos(cupom):.2f}🛒")
                    print("Obrigado por comprar no McDonald's! Volte após sua morte ☺️")
                    break
            elif pergunta.lower() == "n":
                print("Obrigado por comprar no McDonald's! Volte após sua morte ☺️")
                break

print("Olá, bem vindo ao Mcdonald's! 😀")
nome = input("Para começar, digite seu nome ✍️: ")
menu(nome)
