import time

carrinho = []
desconto_aplicado = 0


# Funções Auxiliares
def exibir_opcoes(opcoes):
    """Exibe as opções do menu."""
    for item, valor in opcoes.items():
        print(f"{item}: R${valor:.2f}")


def adicionar_ao_carrinho(opcoes, escolha):
    """Adiciona o item selecionado ao carrinho."""
    for item, valor in opcoes.items():
        if escolha.lower() == item.lower():
            carrinho.append((item, valor))
            print(f"✅ {item} adicionado ao carrinho por R${valor:.2f}!")
            return
    print("❌ Item não encontrado. Tente novamente.")


def remover_do_carrinho():
    """Remove um item do carrinho."""
    if not carrinho:
        print("Seu carrinho está vazio!")
        return
    exibir_carrinho()
    item_para_remover = input("Digite o nome do item que deseja remover: ")
    for i, (item, valor) in enumerate(carrinho):
        if item.lower() == item_para_remover.lower():
            del carrinho[i]
            print(f"🗑️ {item} removido do carrinho.")
            return
    print("❌ Item não encontrado no carrinho.")


def exibir_carrinho():
    """Exibe os itens do carrinho."""
    if not carrinho:
        print("Seu carrinho está vazio!")
    else:
        print("🛒 Itens no carrinho:")
        total = 0
        for item, valor in carrinho:
            print(f" - {item}: R${valor:.2f}")
            total += valor
        print(f"🧾 Total atual: R${total:.2f}")


def aplicar_desconto(cupom):
    """Aplica o desconto baseado no cupom."""
    global desconto_aplicado
    cupons = {
        "ABC5F": 0.05,
        "DEF10G": 0.10,
        "GHI15J": 0.15,
        "KLM20N": 0.20,
    }

    if cupom.upper() in cupons:
        desconto_atual = cupons[cupom.upper()]
        desconto_aplicado = max(desconto_aplicado, desconto_atual)
        print(f"🎉 Cupom {cupom} aplicado! {int(desconto_aplicado * 100)}% de desconto!")
    else:
        print("❌ Cupom inválido!")


def finalizar_compra():
    """Finaliza a compra aplicando desconto."""
    if not carrinho:
        print("Seu carrinho está vazio!")
        return
    exibir_carrinho()
    total = sum(valor for _, valor in carrinho)
    if desconto_aplicado > 0:
        total_com_desconto = total - (total * desconto_aplicado)
        print(f"💰 Desconto aplicado: {int(desconto_aplicado * 100)}%")
        print(f"Valor final com desconto: R${total_com_desconto:.2f}")
    else:
        total_com_desconto = total
        print(f"Valor final: R${total_com_desconto:.2f}")
    print("Obrigado pela sua compra! 🍔 Volte sempre!")


def tempo_preparo():
    """Simula o tempo de preparo dos itens."""
    print("⏳ Preparamos seu pedido, aguarde...")
    time.sleep(2)
    print("Seu pedido está pronto! 🍟")


# Funções de Menu
def menu_lanches():
    lanches = {
        "BigMac": 29.90,
        "McChicken": 27.90,
        "Quarteirão com Queijo": 39.90,
        "McFiesta": 19.90,
        "Chicken Jr": 29.90
    }
    exibir_opcoes(lanches)
    escolha = input("Digite o nome do lanche selecionado 🍔: ")
    adicionar_ao_carrinho(lanches, escolha)
    tempo_preparo()


def menu_sobremesas():
    sobremesas = {
        "McShake": 14.99,
        "Casquinha Baunilha": 4.99,
        "Casquinha Chocolate": 4.99,
        "Sundae Morango": 9.99,
        "Sundae Chocolate": 9.99,
        "Top Sundae Chocolate": 13.99,
        "Top Sundae Morango": 13.99
    }
    exibir_opcoes(sobremesas)
    escolha = input("Digite o nome da sobremesa selecionada 🍨: ")
    adicionar_ao_carrinho(sobremesas, escolha)
    tempo_preparo()


def menu_bebidas():
    bebidas = {
        "Coca-Cola 500ml": 11.90,
        "Sprite 500ml": 10.90,
        "Suco Del Valle Uva 500ml": 8.90,
        "Água 500ml": 1.90
    }
    exibir_opcoes(bebidas)
    escolha = input("Digite o nome da bebida selecionada 🥤: ")
    adicionar_ao_carrinho(bebidas, escolha)
    tempo_preparo()


def menu_combos():
    combos = {
        "McLanche Feliz": 28.90,
        "Family Box para 2": 30.90,
        "Family Box para 3": 39.90
    }
    exibir_opcoes(combos)
    escolha = input("Digite o nome do combo selecionado 🍱: ")
    adicionar_ao_carrinho(combos, escolha)
    tempo_preparo()


def menu_principal(nome):
    while True:
        decisao = input(f"{nome}, você deseja escolher Lanches, Sobremesas, Bebidas, Combos ou ver Carrinho? 🍔🍨🥤🍱: ")

        if decisao.lower() in ["lanches", "lanche"]:
            menu_lanches()
        elif decisao.lower() in ["sobremesas", "sobremesa"]:
            menu_sobremesas()
        elif decisao.lower() in ["bebidas", "bebida"]:
            menu_bebidas()
        elif decisao.lower() in ["combos", "combo"]:
            menu_combos()
        elif decisao.lower() == "carrinho":
            exibir_carrinho()
        elif decisao.lower() == "remover":
            remover_do_carrinho()
        elif decisao.lower() == "finalizar":
            pergunta_cupom = input("Você tem algum cupom? 🎟️ (S/N): ")
            if pergunta_cupom.lower() == "s":
                cupom = input("Digite o código do cupom 🎟️: ")
                aplicar_desconto(cupom)
            finalizar_compra()
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


# Início do programa
print("Olá, bem-vindo ao McDonald's! 🍔")
nome = input("Para começar, digite seu nome ✍️: ")
menu_principal(nome)
