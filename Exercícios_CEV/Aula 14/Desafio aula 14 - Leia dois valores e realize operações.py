'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
import time
print('\033[1;30;46m-=\033[m'*15)
print('\033[1;32;40mBem vindo ao menu matemático do Guanabara!\033[m')
print('\033[1;30;46m-=\033[m'*15)
time.sleep(1.5)

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while True:
    option = str(input('Opções:\n[1]Somar\n[2]Multiplicar\n[3]Maior valor\n[4]Novos números\n[5]Sair do programa\n-->'))
    if option == '1':
        print(f'\033[4;33;40mA soma desses dois valores é: {n1 + n2}\033[m')
    elif option == '2':
        print(f'\033[4;33;40mA multiplicação desses valores é: {n1 * n2}\033[m')
    elif option == '3':
        print(f'\033[4;33;40mO maior valor é {max(n1, n2)}\033[m')
    elif option == '4':
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif option == '5':
        break
    else:
        print('Digite uma opção válida, sua mula!')
print('\nAté mais, fique com o deus da programação! ')
