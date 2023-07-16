'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''

print('Programa para ler números e realizar operações, quase uma calculadora')
print('-='*15)
option = 's'
lista = []
c = 0
total = 1
while option == 's':
    while total >= c:
        n = float(input('Digite um número: '))
        lista.append(n)
        c += 1
    option = str(input('Para digitar mais valores digite s ')).lower()
    if option == 's':
        total = total + int(input('Mais quantos valores você quer digitar: '))

media = sum(lista) / c
print(f'A média desses valores é: {media:.2f}')
print(f'O número {max(lista)} foi o maior valor digitado e o {min(lista)} foi o menor.')