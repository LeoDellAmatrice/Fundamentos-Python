import pandas as pd
import matplotlib.pyplot as plt

# Carrega o dataset a partir da URL
url = "https://raw.githubusercontent.com/LeoDellAmatrice/python-analise-dados/main/valores-grafico.csv"
df = pd.read_csv(url)

# Agrupa os dados pela coluna 'categoria' e soma os valores
gastos_categoria = df.groupby('categoria')['valor'].sum()

# Solicita ao usuário o tipo de gráfico desejado
tipo = input("Digite o tipo de gráfico que deseja (setor, barra, barra_empilhada, linha, dispersao, histograma, caixa, area): ").strip().lower()

# Cria o gráfico com base no tipo selecionado
if tipo == "setor":
    gastos_categoria.plot.pie(autopct="%1.0f%%", startangle=140)
elif tipo == "barra":
    gastos_categoria.plot.bar()
elif tipo == "barra_empilhada":
    # Exemplo simplificado para mostrar como empilhar barras (se houver mais de uma série de dados)
    df.groupby(['categoria', 'subcategoria'])['valor'].sum().unstack().plot.bar(stacked=True)
elif tipo == "linha":
    gastos_categoria.plot.line()
elif tipo == "dispersao":
    # Exemplo simplificado para gráfico de dispersão
    df.plot.scatter(x='coluna_x', y='valor')
elif tipo == "histograma":
    df[' valor'].plot.hist(bins=10)
elif tipo == "caixa":
    df.boxplot(column=[' valor'])
elif tipo == "area":
    gastos_categoria.plot.area()

# Adiciona título e rótulos aos gráficos
plt.title("Gastos Mensais")
plt.ylabel("Valor Total")

# Exibe o gráfico
plt.show()
