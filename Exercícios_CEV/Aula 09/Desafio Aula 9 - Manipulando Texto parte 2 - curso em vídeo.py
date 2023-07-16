'''Faça um programa que leia um número de
0 a 9999 e mostre na tela cada um dos dígitos
separados. Exemplo:
Digite um número: 1834
unidade: 4 ; dezena: 3 ; centena: 8 ; milhar: 1 '''

nome = str(input("Digite seu nome: ")).strip()
nome1 = nome.split()

print(f'Seu primeiro nome é: {nome1[0]} ')
print(f'Seu último nome é: {nome1[len(nome1)-1]}')
print(f'O número de caracter é: {len(nome1)}')