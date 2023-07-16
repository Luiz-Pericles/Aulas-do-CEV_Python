"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
print("Welcome to my program!\nI'll show to you even and odd numbers")
print('-='*20)

list = []
even = []
odd = []
while True:
    n = int(input('Type a number: '))
    list.append(n)
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
    stop = str(input('Want continue? [Y/N]')).upper()
    if stop == 'Y':
        continue
    elif stop == 'N':
        break
    else:
        print('Probably you typed wrong, try again:')
print(f'The main list is {list}')
print(f'The even numbers in list is: {even}')
print(f'The odd numbers in list is: {odd}')
print('\nGoodbye!')
