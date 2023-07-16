"""Desafio 94: Crie um programa que leia nome, sexo e idade de vários pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""
dados = dict()
lista = list()
while True:
    dados['nome'] = str(input('Digite o nome: '))
    dados['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Digite a idade: '))
    lista.append(dados.copy())
    dados.clear()
    option = str(input('Quer cadastrar outro cliente? [S/N] '))
    if option.upper() == 'N':
        break
    elif option.upper() == 'S':
        continue
    while option not in 'SsNn':
        option = str(input('Quer cadastrar outro cliente? [S/N] '))
# Saber quantas pessoas foram cadastradas -->
print(f'\nA) Foram cadastradas {len(lista)} pessoas nesse programa.')
#Para descobrir a média do grupo -->
soma = 0
for item in lista:
    soma += item['idade']
media = soma / len(lista)
print(f"\nB) A média do grupo é: {media}")
#Para descobrir a mulheres do grupo -->
print(f'\nC) As mulheres do grupo são: ', end=(''))
for sexo in lista:
    if sexo['sexo'] == 'F':
        print(f"{sexo['nome']}", end=(' '))
#Para descobrir as pessoas acima da média na idade -->
print(f'\nD) As pessoas com a idade acima da média são: ', end=(''))
for idade in lista:
    if idade['idade'] > media:
        print(f"{idade['nome']}", end=(' '))





