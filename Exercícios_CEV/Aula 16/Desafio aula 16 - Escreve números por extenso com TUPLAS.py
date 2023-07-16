'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = 0
while True:
    n = int(input('Digite um número de 0 a 10: '))
    if n < 0 or n > 10:
        continue
    print(f'Esse número por extenso é {tupla[n]}')
    break
