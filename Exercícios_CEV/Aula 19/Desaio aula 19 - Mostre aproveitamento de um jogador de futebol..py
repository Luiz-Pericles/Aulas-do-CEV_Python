"""Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
#Aqui é criado um dicionário e uma lista. Linha 7 e 8 para adicionar varesumo = dict()
goals = list()
resumo['nome'] = str(input('Digite o nome do jogador de futebol: '))
resumo['partida'] = int(input('Quantas partidas esse jogador jogou: '))

#A partir do input de 'partida' faço um alcance de quantas vezes o código vai executar:
#Cada partida é solicitado o n° de gols e adicionado em uma lista.
for c in range(0, resumo['partida']):
    goals.append(int(input(f"Digite quantos gols {resumo['nome']} fez na partida {c+1}° --> ")))
resumo['gols'] = goals
resumo['Total de gols'] = sum(goals)

print('-=' * 40)
print(resumo)
print('-=' * 40)

for k, v in resumo.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 40)

print(f"O jogador {resumo['nome']} jogou {resumo['partida']} partidas.")
for c in range(0, resumo['partida']):
    print(f'    => Na partida {c+1}, fez {goals[c]}')
print(f'Foi um total de {sum(goals)} goals.')lores no dicionário



