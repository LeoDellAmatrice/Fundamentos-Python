import unicodedata
import webbrowser


def remover_acentos(string):
    nfkd = unicodedata.normalize('NFKD', string)
    string_sem_acentos = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return string_sem_acentos

print("codigo para pesquisar produtos na internet")
qnt_produtos = int(input("digite a quantidade de produtos que deseja pesquisar: "))
produtos = []
for i in range(qnt_produtos):
    p = input("digite o nome do produto: ")
    produtos.append(p)

print(f"otimo, armazenei {len(produtos)} produtos")
sites = []
qnt_sites = int(input("digite a quantidade de sites que deseja pesquisar: "))

for site in range(qnt_sites):
    nome_site = input("digite o endereço do site: ")
    sites.append(nome_site)

print("certo, agora irei abrir o navegador com as informações recebidas")

for site in sites:
    for pr in produtos:
        url = site + "/" + pr
        webbrowser.open_new_tab(url)
