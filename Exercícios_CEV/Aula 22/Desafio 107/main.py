"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


import moeda


p = float(input("Digite o preço R$ "))
print(f'{moeda.aumentar(p, 56)}')
print(f' {moeda.diminuir(p, 13)}')
print(f'\nO dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
