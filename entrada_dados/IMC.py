altura = float(input("digite sua altura em mentros(Ex: 1.72): "))
peso = float(input("digite seu peso em quilos(Ex: 68.5): "))

IMC = peso / (altura * altura)

print(f"com o peso de {peso}kg e com altura de {altura}m o IMC é {IMC:.2f}")