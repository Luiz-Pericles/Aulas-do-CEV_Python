'''Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random
lista = random.randint(0,10)
palpites = 0
while True:
    numero = int(input('Escolha de 0 a 10: '))
    palpites += 1
    if numero == lista:
        break
    elif numero > lista:
        print('Digite um valor menor!')
    elif numero < lista:
        print('Digite um valor maior!')
print(f'\nPara chegar no valor certo você tentou {palpites} vezes')


