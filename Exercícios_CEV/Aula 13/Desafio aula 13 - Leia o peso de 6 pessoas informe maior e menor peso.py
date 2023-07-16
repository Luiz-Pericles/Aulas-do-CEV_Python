'''Faça um programa que leia o peso de 6 pessoas e no final indique qual o maior peso
e o menor peso'''

lista = []
for c in range(0, 6):
    peso = float(input(f'Usuário n°{c+1}, Digite seu peso: '))
    lista.append(peso)
print(f'Esse é o peso usuário mais obeso: {max(lista)}\nEsse é o peso usuário desnutrido: {min(lista)}' )
