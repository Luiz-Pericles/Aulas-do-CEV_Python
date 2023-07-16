"""Desafio 87: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
#Maneira Guanabara:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
            matriz[l][c] = int(input(f"Digite um valor para {l},{c}:  "))
print("-="*20)
for l in range(0,3):
    for c in range(0,3):
            print(f"[{matriz[l][c]:^5}]", end='')
    print()
print('-='*20,'\nNovo Desafio!')
print('-='*20)
somador = []
for c in matriz:
    for p in c:
        if p % 2 == 0:
            somador.append(p)
print(f'A soma de todos os valores PARES da matriz é: {sum(somador)}')
thirdcolun = []
for l in range (0,3):
    thirdcolun.append(matriz[l][2])
print(f'A soma dos termos da terceira coluna é: {sum(thirdcolun)}')
for pos, c in enumerate(matriz):
    if pos == 1:
        print(f'O maior valor da segunda linha é: {max(c)}')
