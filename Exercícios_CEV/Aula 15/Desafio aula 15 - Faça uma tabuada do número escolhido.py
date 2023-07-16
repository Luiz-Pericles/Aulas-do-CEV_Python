'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo'''
print('\033[31;34;40mEsse programa calcula a tabuada do número escolhido\033[m\n\033[31;34;40mDigite um valor negativo para sair\033[m')
multiplicador = 0
while True:
    print('-=' * 15)
    n = int(input('Digite o valor para ser calculado a tabuada: '))
    print('-=' * 15)
    if 0 > n:
        break
    for c in range(0, 11):
        print(f'{n} * {c} = {n*c} ')
print('Goodbye!')

