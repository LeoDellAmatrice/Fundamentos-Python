numero = int(input("digite o numero final da soma de pares: "))
soma = 0


for i in range(numero+1):
    if i % 2 == 0:
        soma += i

print(f"a soma dos pares de 0 a {numero} é: {soma}")
