'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
import random
tupla = (random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20))

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor dessa tupla é: {max(tupla)}')
print(f'O menor valor dessa tupla é: {min(tupla)}')
