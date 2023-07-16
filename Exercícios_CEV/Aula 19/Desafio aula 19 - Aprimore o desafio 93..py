"""Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

"""Desafio 95: Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador."""
#Aqui estou declarando as variáveis que irei trabalhar nesse programa:
jogador = dict()
lista_de_gols = list()
registro_futebol = list()
código_jogador = 1
#Irei montar o sistema de cadastro de jogadores:
while True:
    jogador['código'] = código_jogador
    código_jogador += 1
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f"Quantas partidas o {jogador['nome']} jogou: "))
    for c in range(0, partidas):
        lista_de_gols.append(int(input(f"Digite quantos gols o jogador {jogador['nome']} marcou na partida {c+1}º: ")))
    jogador['gols'] = lista_de_gols.copy()
    jogador['total'] = sum(lista_de_gols)
    lista_de_gols.clear()
    registro_futebol.append(jogador.copy())
    print(registro_futebol)
#Tudo acima é o registro na lista 'registro_futebol', agora irei criar o looping:
    while True:
        option = str(input('Quer cadastrar outro jogador? [S/N] ')).upper()[0]
        if option in 'SN':
            break
        print("ERRO! Únicos valores aceitos são 'Sim' ou 'Não'")
    if option == 'N':
        break
#Com os jogadores cadastrados na lista principal, agora irei mostrar os dados dessa lista:
print("-=" * 30)
print(f"{'Código':<5}  {'Nome':<10}   {'Gols':^8}    {'Total':>20}")
print("-" * 60)
for values in registro_futebol:
    print(f"{values['código']:<5}  {values['nome']:<10}  {values['gols']}   {values['total']:>20}")
#Acima é mostrado os jogadores registrados em um formato de tabela.
#No código abaixo irei fazer o usuário informar o código do jogador e irei informar o aproveitamento do jogador selecionado.
while True:
    buscar = int(input('Digite o código do jogador mais informações ou 999 para sair: '))
    if buscar == 999:
        break
    if buscar > len(registro_futebol):
        print(f"ERRO! Código de jogador inexistente!")
    else:
        for pos, c in enumerate(registro_futebol[buscar-1]['gols']):
            print(f"Na partida {pos+1} o jogador {registro_futebol[buscar-1]['nome']} marcou: {c} gols")
print("Goodbye!")

