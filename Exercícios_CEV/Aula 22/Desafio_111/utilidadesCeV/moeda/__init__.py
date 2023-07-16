"""Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dados.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""


def resumo(valor=0, up=0, down=0,TF=False):
    print("-=" * 30)
    print(f"RESUMO DO VALOR")
    print("-=" * 30)
    print(f'Preço analisado --> {moeda(valor)}')
    print(f'{up}% de aumento --> {aumentar(valor, up, f=TF)}')
    print(f'{down}% de redução --> {diminuir(valor, down, f=TF)}')
    print(f'Dobro do preço --> {dobro(valor, f=TF)}')
    print(f'Metade do preço --> {metade(valor, f=TF)}')
    print("--" * 15)


def aumentar(num, perc, f=False):
    from time import sleep
    #print('-=' * 20)
    #print(f'R${num} será aumentado em {perc}%')
    #print('-->', end='')
    #sleep(2)
    resultado = float(num * (perc/100 + 1))
    if f:
        return moeda(resultado)
    else:
        return resultado


def diminuir(num, perc, f=False):
    from time import sleep
    #print('-=' * 20)
    #print(f'R${num} será diminuindo em {perc}%')
    #rint('-->', end='')
    #sleep(2)
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