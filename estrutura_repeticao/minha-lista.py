import unicodedata
import webbrowser


def remover_acentos(string):
    nfkd = unicodedata.normalize('NFKD', string)
    string_sem_acentos = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return string_sem_acentos


enghaw = [
    "Longe Demais Das Capitais",
    "A Revolta dos Dândis",
    "Ouça o Que Eu Digo: Não Ouça Ninguem",
    "Alívio Imediato",
    "O Papa É Pop",
    "Várias Variáveis",
    "Gessinger, Licks & Maltz",
    "Filmes de Guerra, Canções de Amor",
    "Simples de Coração",
    "Minuano",
    "!Tchau Radar!",
    "10.000 Destinos (Ao Vivo)",
    "Surfando Karmas & DNA",
    "Dançando No Campo Minado",
    "Novos Horizontes (Acústico) (Ao Vivo)",
    "Acústico (Ao Vivo / Deluxe)"
]

sites = [
    "https://lista.mercadolivre.com.br/",
    "https://www.google.com/search?q="
]

for site in sites:
    for eng in enghaw:
        url = site + eng + "-engenheiros"
        webbrowser.open_new_tab(url)
