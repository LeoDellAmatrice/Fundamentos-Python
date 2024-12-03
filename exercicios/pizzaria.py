""" Crie um algoritimo em Python para uma pizarria que trabalha somente com rodizios de pizzas.
Atualmente os valores praticados são por pessoa:
adultos 69,99, crianças até 12 anos 49,99.
junto com o rodizio é oferecido ao cliente alguns vinhos para acompanhamento
conforme tabela por garrafa: Vinho nobre: 29,99, vinho Premium: 46.99.
mas também no cardapio existem as opções: agua: 6.99 refrigerante: lata 9.99, 600ml 12.99.
ao final deve mostrar um relatorio completo."""

despesas_totais = []
valor_total = 0


def mostrar_valores() -> None:
    print("===== ===== Pizzaria Rodízio ===== ====")
    print("===== ===== Valores  Rodízio ===== ====")
    print("||        Adultos        ||  R$69,99 ||")
    print("|| Crianças(até 12 anos) ||  R$49,99 ||")
    print("==== ===== Valores   Vinhos ===== =====")
    print("||      Vinho Nobre      ||  R$29,99 ||")
    print("||     Vinho Premium     ||  R$46,99 ||")
    print("==== ===== Valores  Bebidas ===== =====")
    print("||         Água          ||  R$6,99  ||")
    print("||   Refrigerante Lata   ||  R$9,99  ||")
    print("||   Refrigerante 600ml  ||  R$12,99 ||")
    print("==== ==== ==== ==== ==== ==== ==== ====")


def adicionar_valor(familia: int, pessoas: list[int], adicionais: list[int]) -> None:
    despesas_totais.append([f'{familia}', pessoas, adicionais])
    return


def relatorio():
    global valor_total
    for familia in range(0, len(despesas_totais)):
        print(f"familia: {int(despesas_totais[familia][0]) + 1}:")
        print(f"==== === === = Rodízio = === === ====")
        for pessoa in range(0, len(despesas_totais[familia][1])):
            if despesas_totais[familia][1][pessoa] == 1:
                print(f"|| Criança: R$49.99                ||")
                valor_total += 49.99
            else:
                print(f"|| Adulto: R$69.99                 ||")
                valor_total += 69.99
        print(f"==== == === == Bebidas == === == ====")
        for bebida in range(0, len(despesas_totais[familia][2])):
            if despesas_totais[familia][2][bebida] == 0:
                print(f"|| {bebida+1} - Vinho Nobre: R$29,99        ||")
                valor_total += 29.99
            elif despesas_totais[familia][2][bebida] == 1:
                print(f"|| {bebida+1} - Vinho Premium: R$46,99      ||")
                valor_total += 46.99
            elif despesas_totais[familia][2][bebida] == 2:
                print(f"|| {bebida+1} - Água: R$6.99                ||")
                valor_total += 6.99
            elif despesas_totais[familia][2][bebida] == 3:
                print(f"|| {bebida+1} - Refrigerante Lata: R$9,99   ||")
                valor_total += 9.99
            elif despesas_totais[familia][2][bebida] == 4:
                print(f"|| {bebida+1} - Refrigerante 600ml: R$12,99 ||")
                valor_total += 12.99
        print(f"======= Valor total: R${valor_total:.2f} =======\n\n")
    return


def main():
    mostrar_valores()
    quant_familias = int(input("Informe quantas familias foram à pizaria: "))
    for familia in range(quant_familias):
        quant_pessoas = int(input(f"Informe quantas pessoas tem na {familia+1}º familia: "))
        pessoas = []
        for i in range(quant_pessoas):

            pessoas.append(int(input("====\n1 - adulto\n2 - criança\nDigite: "))-1)

        adicionais = []

        numero_adicionais = int(input("Digite quantos acompanhamentos compraram: "))

        for i in range(numero_adicionais):
            adicionais.append(int(input("====\n1 - Vinho Nobre\n2 - Vinho Premium\n3 - Água\n4 - refrigerante Lata\n5 - Refrigerante 600ml\nDigite: "))-1)

        adicionar_valor(familia, pessoas, adicionais)
    relatorio()


main()
