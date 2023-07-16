"""Desafio 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários."""

from utilidadesCeV import moeda
from utilidadesCeV import dado


p = dado.leiaDinheiro("Digite o preço R$ ")
moeda.resumo(p, 100, 20, True)
#print(f'{moeda.aumentar(p, 56, True)}')
#print(f' {moeda.diminuir(p, 13, True)}')
#print(f'\nO dobro de R${p} é {moeda.dobro(p, True)}')
#print(f'A metade de R${p} é {moeda.metade(p, True)}')
