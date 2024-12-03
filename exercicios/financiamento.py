from tabulate import tabulate
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calcula_imovel(vt, anos, renda):
    parcelas = [
        ["Parcela", "data", "Valor"],
    ]
    qp = anos * 12
    custo_adicional = (vt / qp) + (vt * 0.05)
    parcela = vt / qp
    if parcela > renda * 0.30:
        print("Renda insuficiente para parcelas.")
        print("encerrando programa...")
        exit()
    print(f"o custo adicional de documentação é de: {custo_adicional:.2f}")
    escolha = int(input("digite 1 para dividir o custo entre todas as parcelas\n"
                        "digite 2 para adicionar o custo apenas na 10º parcela: "))
    dia = int(input("Digite o dia de vencimento das parcelas: "))
    if escolha == 1:
        custo_adicional = custo_adicional / qp
        for i in range(qp):
            data = datetime(2024, 10, dia)
            data = data + relativedelta(months=i + 1)
            parcelas.append([f"Parcela {i + 1}", f"{data.date()}", f"{parcela:.2f}"])
    elif escolha == 2:
        for i in range(qp):
            data = datetime(2024, 10, dia)
            data = data + relativedelta(months=i + 1)
            if i == 9:
                parcelas.append([f"Parcela {i + 1}", f"{data.date()}", f"{parcela + custo_adicional:.2f}"])
            else:
                parcelas.append([f"Parcela {i + 1}", f"{data.date()}", f"{parcela:.2f}"])

    return parcelas


def calcula_veiculo(vt, anos, juros, renda):
    parcelas = [
        ["Parcela", "data", "Valor"],
    ]
    qp = anos * 12
    parcela = (vt + (vt * juros)) / qp
    if parcela > renda * 0.30:
        print("Renda insuficiente para parcelas.")
        print("encerrando programa...")
        exit()
    dia = int(input("Digite o dia de vencimento das parcelas: "))
    for i in range(qp):
        data = datetime(2024, 10, dia)
        data = data + relativedelta(months=i + 1)
        parcelas.append([f"Parcela {i + 1}", f"{data.date()}", f"{parcela:.2f}"])
    return parcelas


def tabela_parcelas(parcelas):
    print(tabulate(parcelas, headers="firstrow", tablefmt="grid"))


print("...Bem-vindo ao financiamento automático...")
renda = float(input("digite sua renda: "))
tipo = input("deseja calcular o financiamento para veículo ou imóvel? ")

if tipo in ["imovel", "Imovel", "imóvel", "Imóvel"]:
    print("...financiamento para imóvel...")
    vt = float(input("Digite o valor total do imóvel: "))
    anos = int(input("Digite em quantos anos deseja pagar: "))

    tabela_parcelas(calcula_imovel(vt, anos, renda))

elif tipo in ["veiculo", "Veiculo", "Veículo", "veículo"]:
    print("...financiamento para veículos...")
    vt = float(input("Digite o valor total do veículo: "))
    anos = int(input("Digite em quantos anos deseja pagar: "))
    km = input("o carro que deseja financiar é 0km(s/n)? ")
    if km == "n":
        idade = int(input("Digite a idade do veículo: "))

    if km == "s":
        juros = 0.005
    elif idade < 24:
        juros = 0.019
    else:
        juros = 0.025

    tabela_parcelas(calcula_veiculo(vt, anos, juros, renda))
else:
    print("Tipo de financiamento inválido.")
