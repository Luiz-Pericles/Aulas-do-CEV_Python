"""Desafio 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na
na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

import moeda


p = float(input("Digite o preço R$ "))
moeda.resumo(p, 100, 20, True)
#print(f'{moeda.aumentar(p, 56, True)}')
#print(f' {moeda.diminuir(p, 13, True)}')
#print(f'\nO dobro de R${p} é {moeda.dobro(p, True)}')
#print(f'A metade de R${p} é {moeda.metade(p, True)}')
