"""Desafio 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
lista = []
par = []
impar = []
for c in range(0,7):
    n = int(input(f'Digite o {c+1}ºnúmero: '))
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
lista.append(par[:])
lista.append(impar[:])
print(f'Os números pares digitados foram: {sorted(lista[0])}')
print(f'Os números ímpares digitados foram: {sorted(lista[1])}')

