"""Desafio 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

import moeda


p = float(input("Digite o preço R$ "))
print(f'{moeda.aumentar(p, 56, True)}')
print(f' {moeda.diminuir(p, 13, True)}')
print(f'\nO dobro de R${p} é {moeda.dobro(p, True)}')
print(f'A metade de R${p} é {moeda.metade(p, True)}')
