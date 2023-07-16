'''Desafio 76: Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''
tupla = ('eu', 'conheci', 'uma', 'americana', 'la', 'na', 'vaquejada', 'e', 'ela', 'dizia', 'assim', 'were burning up')
for palavra in tupla:
    print(f'\nNa palavra \033[1;32;40m{palavra}\033[m as vogais são: ', end=(''))
    for c in palavra:
        if  c in 'aeiou' :
            print(f'{c}', end=(' '))
