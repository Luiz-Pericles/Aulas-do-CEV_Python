"""Desafio 86: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
#Maneira como fiz:
'''dados = []
for c in range(0,3):
    dados.append(int(input(f"Digite o valor 0,{c}: ")))
for c in range(0,3):
    dados.append(int(input(f"Digite o valor 1,{c}: ")))
for c in range(0, 3):
    dados.append(int(input(f"Digite o valor 2,{c}: ")))
print(f'[{dados[0]}] [{dados[1]}] [{dados[2]}]  ')
print(f'[{dados[3]}] [{dados[4]}] [{dados[5]}]  ')
print(f'[{dados[6]}] [{dados[7]}] [{dados[8]}]  ')'''

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
