"""Desafio 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente."""
print('Welcome to program')
valores = []
while True:
    n = int(input('Digite o valor: '))
    if n in valores:
        print('Valor duplicado, NÃO adicionado')
    else:
        valores.append(n)
        print('Valor adicionado!')
    continuar = str(input('Quer continuar [S/N}: ')).upper()
    if continuar == 'N':
        break

print(sorted(valores))
print('Goodbye!')
