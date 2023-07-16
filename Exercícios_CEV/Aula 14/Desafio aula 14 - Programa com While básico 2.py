'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.(Desconsiderando o flag).'''
print('Bem-vindo ao programa básico python 2!')
print('-='*15)
print('Para sair digite: 999')
n = int(input('Digite um número: '))

c = 0
s = n
while True:
    n = int(input('Digite um número: '))
    c += 1
    if n == 999:
        break
    s = s + n

print(f'Você digitou {c} vezes! E a soma dos valores digitados é: {s}')