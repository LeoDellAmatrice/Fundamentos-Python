reais = float(input("digite quantos reais deseja converter: "))
dolar = reais / 5.64

if dolar > 5000:
    taxa = (dolar - 5000) * 0.15
    print(f"a conversão de R${reais:.2f} para dolar resultou em ${dolar:.2f} \n"
          f"e taxa de $0.15 por dolar acima de $5.000 que foi de ${taxa:.2f}")
else:
    print(f"a conversão de R${reais:.2f} para dolar resultou em ${dolar:.2f}")
