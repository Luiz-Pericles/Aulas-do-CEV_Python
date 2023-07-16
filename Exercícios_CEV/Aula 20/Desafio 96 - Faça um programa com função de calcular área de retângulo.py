"""Desafio 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular(largura e comprimento) e mostre a área do terreno."""
def título(msg):
    print("-=" * 30)
    print(msg)
    print("-=" * 30)

def área(larg, comp):
    a = larg * comp
    print(f"A área desse terreno com comprimento {c} metros e largura {l} metros é de {a}m²")

#Main function:
título("Boas-vindas ao programa calculador de áreas de terrenos alheios")
l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))
área(l, c)


