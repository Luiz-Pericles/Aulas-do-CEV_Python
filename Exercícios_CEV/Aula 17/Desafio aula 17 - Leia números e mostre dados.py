"""Desafio 81: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

print('Hello, Welcome to my program with list in python!')
print('-=' * 20)

lista = []
n = int(input('Type a number: '))
lista.append(n)
while True:
    p = str(input('Want continue? [Y/N]')).upper()
    if p == 'Y':
        n = int(input('Type a number: '))
        lista.append(n)
    elif p == 'N':
        break
    else:
        print('Probably you typed wrong! Again:')
print(f'The length of list is {len(lista)} numbers')
print(f'The list in reverse sequence is {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'In list has a five(5) typed, in {sorted(lista, reverse=True).index(5) + 1} position')
else:
    print(f"Doesn't have any five(5) in this list")
