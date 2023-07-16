"""Desenvolva um programa que leia 6 números e some apenas os que forem pares."""

s = 0
for c in range(0,6):
    n1 = int(input("Digite um número: "))
    if n1 % 2 == 0:
        s += n1
print(s)
