kilometros = int(input("digite quantos Km tem a viagem: "))
MEDIA_KM_LTS_GASOLINA = 10
MEDIA_KM_LTS_ETANOL = 7
VALOR_LITRO_GASOLINA = 5.69
VALOR_LITRO_ETANOL = 3.49

qtde_litros_gasolina = kilometros / MEDIA_KM_LTS_GASOLINA
qtde_litros_etanol = kilometros / MEDIA_KM_LTS_ETANOL

valor_gasto_gasolina = qtde_litros_gasolina * VALOR_LITRO_GASOLINA
valor_gasto_etanol = qtde_litros_etanol * VALOR_LITRO_ETANOL

print(f"o valor gasto de gasolina é de R${valor_gasto_gasolina:.2f} e o gasto com etanol é de R${valor_gasto_etanol:.2f} ")