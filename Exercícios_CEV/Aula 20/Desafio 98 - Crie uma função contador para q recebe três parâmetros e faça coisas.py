"""Desafio 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada."""
from time import sleep

def contador():
    #A)
    print("-=" *30)
    for a in range(0, 11, 1):
        print(a, end=(" "))
        sleep(0.2)
    print()
    print("-=" * 30)
    #B)
    for b in range(10, -1, -2):
        print(b, end=(" "))
        sleep(0.2)
    print()
    print("-=" * 30)
    #C)
    start = int(input("ínicio: "))
    end = int(input("Fim: "))
    step= int(input("Passo: "))
    if step < 0:
        end = end - 2
    elif step == 0:
        step = 1
    for c in range(start, end+1, step):
        print(c, end=(" "))
        sleep(0.2)
    print()
    print("-=" * 30)
    print("Fim!")


#main function:
contador()






