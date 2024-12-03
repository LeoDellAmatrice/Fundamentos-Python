colaborador_nome = "Leonardo Dell'Amatrice"
empresa = "Senai"
salario = 3456.90
percentual = 7
valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print(f"O colaborador {colaborador_nome}, trabalha na empresa {empresa} e foi promovido com novo salario"
      f"de R$ {novo_salario:.2f}")