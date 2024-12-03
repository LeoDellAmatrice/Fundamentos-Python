numeros = [
    6, 34, 73, 87, 234, 9, 34
]

print(numeros)
mult = int(input("digite um valor que deseja multiplicar cada valor da lista: "))

for i in range(len(numeros)):
    numeros[i] *= mult

print(numeros)
