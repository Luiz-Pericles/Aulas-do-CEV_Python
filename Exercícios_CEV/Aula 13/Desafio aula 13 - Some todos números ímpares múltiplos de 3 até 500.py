"""Faça um programa que some todos os números de 1 até 500 que são ímpares e multiplos de 3"""
s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        contador += 1
        print(c, end= ' ')
print(f'\nA soma é {s}\nE a quantidade de valores foi: {contador}')


