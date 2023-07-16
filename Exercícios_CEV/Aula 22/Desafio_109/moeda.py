"""Desafio 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""


def aumentar(num, perc, f=False):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será aumentado em {perc}%')
    print('-->', end='')
    sleep(2)
    resultado = float(num * (perc/100 + 1))
    if f:
        return moeda(resultado)
    else:
        return resultado


def diminuir(num, perc, f=False):
    from time import sleep
    print('-=' * 20)
    print(f'R${num} será diminuindo em {perc}%')
    print('-->', end='')
    sleep(2)
    resultado = float(num * (1 - perc/100))
    if f:
        return moeda(resultado)
    else:
        return resultado


def dobro(num, f=False):
    if f:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, f=False):
    if f:
        return moeda(num/2)
    else:
        return num / 2


def moeda(preço=0, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

