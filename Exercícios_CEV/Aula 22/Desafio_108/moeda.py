"""Desafio 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado."""


def aumentar(num, perc):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será aumentado em {perc}%')
    print('-->', end='')
    sleep(2)
    resultado = float(num * (perc/100 + 1))
    return resultado


def diminuir(num, perc):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será diminuindo em {perc}%')
    print('-->', end='')
    sleep(2)
    resultado = float(num * (1 - perc/100))
    return resultado


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def moeda(preço=0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

