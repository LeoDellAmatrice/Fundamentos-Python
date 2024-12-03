cds = [
    'Longe demais das captais', 'Ouça o que eu digo não ouça ninguem', 'Varias variaveis',
    'Surfando karmas & DNA', 'dançando no campo minado'
]

for i, cd in enumerate(cds):
    print(f'{i+1} - {cd}')

escolha = int(input('Escolha um álbum: '))

if 1 <= escolha <= len(cds):
    print(f'Você escolheu o álbum: {cds[escolha-1]}')