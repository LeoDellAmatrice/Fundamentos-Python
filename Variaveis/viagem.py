carro = "fiat uno 3.0 manual"
VALOR_LITRO_GASOLINA = 5.69
VALOR_LITRO_ETANOL = 3.49

cidade_saida = "Piracicaba"
cidade_destino = "Campinas"
kilometros = 75
MEDIA_KM_LTS_GASOLINA = 10
MEDIA_KM_LTS_ETANOL = 7

qtde_litros_gasolina = kilometros / MEDIA_KM_LTS_GASOLINA
qtde_litros_etanol = kilometros / MEDIA_KM_LTS_ETANOL

valor_gasto_gasolina = qtde_litros_gasolina * VALOR_LITRO_GASOLINA
valor_gasto_etanol = qtde_litros_etanol * VALOR_LITRO_ETANOL

print(f"A distancia entre {cidade_saida} e {cidade_destino} é de {kilometros}KM\n"
      f"Será gasto R$ {valor_gasto_gasolina:.2f} com gasolina e R$ {valor_gasto_etanol:.2f} com etanol")