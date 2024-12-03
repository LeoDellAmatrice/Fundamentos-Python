distancia = int(input("digite quantos KM deseja viajar"))

if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50

print(f'o preço da sua viagem será de R${preco}')
