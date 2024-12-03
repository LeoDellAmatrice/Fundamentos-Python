valor_financiado = float(input("digite o valor a ser financiado: "))
anos = int(input("digite a quantidade de anos que deseja fazer o financiamento: "))

valor_parcela = valor_financiado / (anos * 12)

print(f"o valor de cada parcela é de {valor_parcela:.2f}. "
      f"O valor financiado foi de R${valor_financiado:.2f} em {anos} anos")
