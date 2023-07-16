"""Desafio 100: faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteia():
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        number = randint(0, 10)
        print(f'{number}', end=' ')
        sleep(0.5)
        numeros.append(number)
    print('PRONTO!')


def somar_par():
    somador = 0
    for values in numeros:
        if values % 2 == 0:
            somador += values
    print(somador)


numeros = list()
sorteia()
print(f'Somando os valores pares de {numeros}, temos -->', end=' ')
somar_par()
