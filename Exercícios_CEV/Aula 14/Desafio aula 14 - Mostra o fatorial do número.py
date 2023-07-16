'''Faça um programa que leia número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120'''
n = int(input('Digite o número vai ser calculado o fatorial: '))
c = n
f = 1
print(f'O fatorial de {n}! = ', end=(''))
while c > 0:
    f = f * c
    print(f'{c} x ', end=(''))
    c -= 1
    if 1 == c:
        print(f'{c} = {f}', end=(''))
        break
#Feito com a função 'for', porém a aula é 'while'.
'''numero = int(input('Digite o número que vai ser calculado o fatorial: '))
print('O fatorial desse número é: ')
print(numero, end=(''))
for d in range(numero-1, 0, -1):
    print(f'x{d}', end=(''))
for c in range(numero-1, 0, -1):
    numero = numero * c
print(f' = {numero}', end=(''))'''
#Lembrando que essa função pode ser feita simplesmente importando o módulo 'math':
'''from math import factorial
n = int(input('Digite o número que vai ser calculado o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n}! é igual a {f}')'''
