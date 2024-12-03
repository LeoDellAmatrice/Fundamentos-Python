print("calcular a media do aluno")
nome = input("Digite o nome do aluno: ")
notas = []

for i in range(0, 5):
    if i < 2:
        nota = float(input(f"Digite a nota da {i+1}º prova: "))
    elif i >= 2:
        nota = float(input(f"Digite a nota do {i - 1}º exercicio: "))
    notas.append(nota)

notas[0] = notas[0] * 0.4
notas[1] = notas[1] * 0.3
notas[2] = notas[2] * 0.15
notas[3] = notas[3] * 0.08
notas[4] = notas[4] * 0.07

media = sum(notas)

print(f"Nome do aluno: {nome}")
print(f"Média das notas: {media:.2f}")
print("Notas após a aplicação dos pesos:")
for i in range(0, 5):
    print(f"{i+1}º nota: {notas[i]:.2f}")

faltas = int(input(f"o aluno {nome} faltou quantas vezes? "))

if faltas > 5:
    media -= 5
    print(f"como o aluno {nome} faltou mais que 5 vezes,\nfoi descontado 5 pontos da media, a media agora é de: {media}")
else:
    print(f"o aluno {nome} não foi descontado devido a quantidade de faltas.")
    print(f"a media final do aluno {nome }foi de: {media}")
