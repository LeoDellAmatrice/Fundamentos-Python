inicio = int(input("digite um numero para iniciar a soma: "))
fim = int(input("digite um numero para terminar a soma: "))

soma = 0

for i in range(inicio, fim+1):
    soma += i

print(f"a soma dos numeros entre {inicio} e {fim} é {soma}")
