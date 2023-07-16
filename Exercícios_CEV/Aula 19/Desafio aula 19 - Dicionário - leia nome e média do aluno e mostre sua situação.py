"""Desafio 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela"""
escola = dict()
escola['Nome'] = str(input("Digite o nome do aluno: "))
escola['Média'] =  float(input(f"Digite a média do aluno {escola['Nome']}: "))
if escola['Média'] >= 7:
    escola['Situação'] = 'APROVADO'
elif escola['Média'] < 7:
    escola['Situação'] = 'REPROVADO'
for k, v in escola.items():
    print(f'O {k} é {v}')
