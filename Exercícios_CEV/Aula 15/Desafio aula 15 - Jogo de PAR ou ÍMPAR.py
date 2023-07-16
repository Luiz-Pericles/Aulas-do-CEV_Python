'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print('-='*15)
print('Bem-vindo ao jogo de PAR ou ÍMPAR\nEu sou a máquina e irei jogar com você!')
print('-='*15)

import random
c = 0
while True:
    escolha = str(input('Digite 0 para PAR ou 1 para ímpar: '))
    if escolha == '0':
        máquina = random.randint(0,10)
        jogador = int(input('Digite seu número de 0 a 10: '))
        resultado = (máquina + jogador) % 2
        if resultado == 0:
            c = c + 1
            print(f'Parabéns + 1 ponto, a máquina escolheu {máquina}')
        else:
            print(f'Que pena! A máquina escolheu {máquina} e você perdeu.')
            print(f'Você ganhou {c} vezes!')
            break
    if escolha == '1':
        máquina = random.randint(0,10)
        jogador = int(input('Digite seu número de 0 a 10: '))
        resultado = (máquina + jogador) % 2
        if resultado == 1:
            c = c + 1
            print(f'Parabéns + 1 ponto, a máquina escolheu {máquina}')
        else:
            print(f'Que pena! A máquina escolheu {máquina} e você perdeu.')
            print(f'Você ganhou {c} vezes!')
            break
