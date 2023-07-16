"""Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome, gols=0):
    print('-=' * 30)
    if nome.strip() == "":
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


a = str(input('Digite o nome do jogador: '))
b = str(input('Digite quantos gols esse jogador marcou: '))
print(ficha(a, b))
