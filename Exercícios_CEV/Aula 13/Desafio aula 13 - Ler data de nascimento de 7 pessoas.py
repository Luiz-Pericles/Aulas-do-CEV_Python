'''Crie um programa que leia a data de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade(21) e quantas já são maiores.'''

import datetime
lista = []
lista2 = []

for c in range(0, 3):
    nome = str(input('Digite seu nome: '))
    data = int(input('Em que ano você nasceu: '))
    idade = datetime.date.today().year - data
    if idade >= 21:
        lista.append(nome)
    else:
        lista2.append(nome)

print(f'\nAs pessoas que já atingiram a maioridade são: {lista}')
print(f'\nE as pessoas que ainda não atingiram a maioridade são: {lista2}')
