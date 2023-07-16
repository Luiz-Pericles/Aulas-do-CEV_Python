'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
print('Programa de Fibonacci!')
print('-='*15)
termos = int(input('Quantos termos você quer mostrar: '))
c = 3
a1 = 0
a2 = 1
print(f'{a1} -> {a2} -> ', end=(''))
while termos >= c:
    a3 = a2 + a1
    print(f'{a3} -> ', end=(''))
    a1 = a2
    a2 = a3
    c += 1
print('FIM!')