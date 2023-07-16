"""Desafio 104: Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaint('Digite um n')"""


def leiaint(msg=''):
    x = str(input(msg))
    while not x.isnumeric():
        print(f'Erro! Número digitado não foi numérico.')
        x = str(input(msg))
    return x



# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
