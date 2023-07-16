"""Desafio 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado."""

import moeda


p = float(input("Digite o preço R$ "))
print(f'{moeda.moeda(moeda.aumentar(p, 56))}')
print(f' {moeda.moeda(moeda.diminuir(p, 13))}')
print(f'\nO dobro de R${p} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de R${p} é {moeda.moeda(moeda.metade(p))}')
