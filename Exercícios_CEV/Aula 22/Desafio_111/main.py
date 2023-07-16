"""Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dados.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""


from utilidadesCeV import moeda


p = float(input("Digite o preço R$ "))
moeda.resumo(p, 100, 20, True)
#print(f'{moeda.aumentar(p, 56, True)}')
#print(f' {moeda.diminuir(p, 13, True)}')
#print(f'\nO dobro de R${p} é {moeda.dobro(p, True)}')
#print(f'A metade de R${p} é {moeda.metade(p, True)}')
