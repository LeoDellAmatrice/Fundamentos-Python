# Você foi contratado para criar um algoritmo que verifique se o cliente tem renda suficiente para conseguir
# aprovação em um crédito imobiliário, a parcela mensal do valor do imóvel não pode ultrapassar 30% da
# renda do cliente.


# Definindo as variáveis
renda_cliente = 6000  # Renda do cliente em reais
valor_imovel = 150000  # Valor do imóvel em reais
tempo_anos = 12
parcela_mensal = valor_imovel / (tempo_anos*12)

if parcela_mensal <= (renda_cliente * 0.3):
    print('Cliente possui renda suficiente para conseguir aprovação.')
    print(f'Parcela mensal do imóvel: R$ {parcela_mensal:.2f}')
else:
    print('Cliente não possui renda suficiente para conseguir aprovação.')
    print(f'Parcela mensal do imóvel ultrapassa 30% da renda do cliente: R$ {parcela_mensal:.2f}')
