def calcular_investimento(risco, meses):
    if risco.lower() == "baixo":
        if meses == 24:
            return "AZ investimentos", 0.5
        elif meses == 60:
            return "AZ investimentos", 0.8
        elif meses == 120:
            return "AZ investimentos", 1.2
        else:
            return "Erro ao calcular"
    elif risco.lower() == "medio":
        if meses == 24:
            return "Crypto invest", 1.1
        elif meses == 60:
            return "Crypto invest", 1.5
        elif meses == 120:
            return "Crypto invest", 1.9
        else:
            return "Crypto invest", "Erro ao calcular(verifique a entrada de valor)"
    elif risco.lower() == "alto":
        if meses == 24:
            return "Bitcoin XP", 2.1
        elif meses == 60:
            return "Bitcoin XP", 2.8
        elif meses == 120:
            return "Bitcoin XP", 3.9
        else:
            return "Bitcoin XP", "Erro ao calcular(verifique a entrada de valor)"
    else:
        return "Risco inválido"


risco_investimento = input("Digite o risco (baixo, medio ou alto): ")
quantidade_meses = int(input("Digite a quantidade de meses(24, 60 ou 120): "))
empresa, rentabilidade = calcular_investimento(risco_investimento, quantidade_meses)
print(f"A empresa escolhida é {empresa} e a rentabilidade é de {rentabilidade}% ao mês")
montante = float(input("digite o quanto deseja investir: "))*(1 + rentabilidade/100)**quantidade_meses
print(f"O montante total após {quantidade_meses} meses é de {montante:.2f}")
