"""Desafio 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    lista.append(n)
print('-=-'*15)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor dessa lista é: {max(lista)}, e esta na posição: ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')

print(f'\nO menor valor dessa lista é: {min(lista)}, e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print('\nGoodbye!')
