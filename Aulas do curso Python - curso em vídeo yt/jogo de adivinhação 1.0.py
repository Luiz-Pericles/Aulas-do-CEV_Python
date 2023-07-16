import random
lista = random.randint(0, 5)

numero = int(input('Escolha um número de 0 a 5: '))
if numero == lista:
    print('Você acertou o número que o computador pensou!')
else:
    print('Você errou o número')

print(f'Esse foi o número que o computador pensou: {lista}')