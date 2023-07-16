"""Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""


def aumentar(num, perc):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será aumentado em {perc}%')
    print('--> R$', end='')
    sleep(2)
    resultado = float(num * (perc/100 + 1))
    return resultado


def diminuir(num, perc):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será diminuindo em {perc}%')
    print('--> R$', end='')
    sleep(2)
    resultado = float(num * (1 - perc/100))
    return resultado


def dobro(num):
    return num * 2


def metade(num):
    return num / 2
