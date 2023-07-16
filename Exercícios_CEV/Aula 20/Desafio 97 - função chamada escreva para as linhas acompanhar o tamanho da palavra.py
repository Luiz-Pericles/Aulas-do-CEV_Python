"""Desafio 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
 mostre uma mensagem com tamanho adaptável.
 Ex: escrava('Olá, Mundo!')
 Saída: -----------
        Olá, Mundo!
        -----------"""


def escreva(x):
    print("-" * len(msg))
    print(x)
    print("-" * len(msg))


msg = str(input("Digite seu texto: "))
escreva(msg)
