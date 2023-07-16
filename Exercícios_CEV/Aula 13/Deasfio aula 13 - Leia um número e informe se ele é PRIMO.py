"""Leia um número e informe se o mesmo é um número primo"""

#Variável teste funciona assim, se finalizar igual 2 o número é primo
teste = 0

n = int(input("Digite o número: "))

for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        teste = teste + 1
    else:
        print('\033[31m', end=' ')
    print(c, end='')
if teste == 2:
    print("\nEsse número é PRIMO")
else:
    print("\nEsse número não é primo")

