"""Faça um programa que apresente o menu de opções a seguir:
1. Média aritmética
2. Média ponderada
3. Sair
Digite a opção desejada
Na opção 1: receber duas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada.
Na opção 3: Sair do programa.
Verifique a possibilidade de opção inválida. Neste caso, o programa deverá mostrar uma mensagem."""

#Boas-vindas do código.
import time
print('\033[1;30;46m-=\033[m'*15)
print('\033[1;32;40mBem vindo ao menu matemático!\033[m')
print('\033[1;30;46m-=\033[m'*15)
time.sleep(1.5)

menu = '0'
while True:
# Aqui abre o menu de seleção para o usuário
    menu = str(input('\n1-[Média arimética]\n2-[Média ponderada}\n3-[sair}\n--> '))
    if menu == '1':
        m1 = float(input('Digite o primeiro valor: '))
        m2 = float(input('Digite o segundo valor: '))
        mediaa = (m1 + m2) / 2
        print(f'A média aritmética desses dois valores é: {mediaa}')
    elif menu == '2':
        nota1 = float(input('Digite a primeira nota: '))
        peso1 = float(input('Digite o peso da primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        peso2 = float(input('Digite o peso da segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        peso3 = float(input('Digite o peso da terceira nota: '))
        mediap = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / 3
        print(f'A média ponderada é: {mediap}')
    elif menu == '3':
        break
    else:
        print('Opção inválida, digite: ')

print('Goodbye!')
