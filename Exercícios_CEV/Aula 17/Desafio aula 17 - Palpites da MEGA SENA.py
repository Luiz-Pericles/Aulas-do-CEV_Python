"""Desafio 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

import random
import time
print("-="*20,"\n\033[1;32;40mJOGUIN DA MEGA SENA SUAVE!\033[m")
print("-="*20)

jogos = []
npalpites = []
j = int(input("How many games do you want to play? "))
time.sleep(1.5)
for c in range(0,j):
    for p in range (0,6):
        npalpites.append(random.randint(1,60))
    jogos.append(npalpites[:])
    npalpites.clear()
print(f"Calm down, I'll show to you {j} palpites for the game")
for c in range(0,j):
    print(f'Jogo {c+1}: {jogos[c]}')
    time.sleep(1)
print("\nGood lucky and don't get addicted!")

