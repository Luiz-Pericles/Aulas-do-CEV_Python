"""Desafio 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial."""


def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show and c == 1:
            print(f'{c} = ', end='')
        elif show:
            print(f'{c}x', end='')
    return f


n = int(input('Digite o número que deseja calcular o fatorial: '))
print('=-' * 30)
print(fatorial(n, show=True))
help(fatorial)
