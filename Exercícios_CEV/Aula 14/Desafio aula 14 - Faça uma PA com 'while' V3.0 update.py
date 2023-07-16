'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''
print('Programa de cálculo de uma PA')
print('-='*15)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
contador = 1
total = 10
mais = total
while mais != 0:
    while total >= contador:
        print(f'{primeiro} -> ', end=(''))
        primeiro += razão
        contador += 1
    print('PAUSA!')
    mais = int(input('\nDigite quantos termos você quer aumentar: '))
    total = total + mais
print('FIM!')