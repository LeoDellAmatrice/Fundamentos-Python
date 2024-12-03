
def calcularimc(pe, alt):
    return pe / (alt ** 2)


def tabelaimc(imc: float):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Acima do peso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


peso = float(input("digite o seu peso(Kg): "))
altura = float(input("digite a sua altura(m): "))
print(f"seu imc: {calcularimc(peso, altura):.2f} \nclassificação: {tabelaimc(calcularimc(peso, altura))}")
