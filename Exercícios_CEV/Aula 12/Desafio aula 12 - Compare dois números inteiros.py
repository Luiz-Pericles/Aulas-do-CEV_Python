'''Faça um programa que compare dois números inteiros informando se um número é maior ou menor ou se
são iguais'''

n1 = int(input('Olá, bem-vindo ao programa! Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print(f'O {n1} é maior que o {n2}!')

elif n1 < n2:
    print(f'O {n2} é maior que o {n1}!')

elif n1 == n2:
    print(f'Os dois números são iguais!')   