def calculadora(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Divisão por zero não é permitida"
        else:
            return n1 / n2
    else:
        return "Operação inválida"


numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

result = calculadora(numero1, numero2, operacao)
print(f"Resultado da operação: {result}")
