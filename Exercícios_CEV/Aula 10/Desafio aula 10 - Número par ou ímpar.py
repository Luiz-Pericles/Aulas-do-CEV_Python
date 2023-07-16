#Crie um programa para ler se o número é par ou ímpar.

numero = int(input('Digite um número: '))
teste = numero % 2
if teste == 0:
    print(f'O número {numero} é um número par')
else:
    print(f'O número {numero} é um número ímpar')

print('\nIt is all, folks!')
