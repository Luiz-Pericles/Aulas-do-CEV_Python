"""Desafio 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual ]
será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui as cédulas de R$50, R$20, R$10 e R$1."""
#Método Matemático Luiz:
print('-='*15)
print("Bem-vindo ao caixa eletrônico, MAKE THE 'L' ")
print('-='*15)
n = int(input('Digite o valor do saque: '))
a = n // 50
b = (n - 50*a) // 20
c = (n - 50*a - 20*b) // 10
d = (n - 50*a - 20*b - 10*c) // 1
print(f'Para sacar {n} foram precisos é precisso {a} notas de 50, {b} notas de 20, {c} notas de 10 e {d} nota de 1')
