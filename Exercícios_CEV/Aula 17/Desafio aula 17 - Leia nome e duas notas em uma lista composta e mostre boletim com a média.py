"""Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente."""

aluno = []
dados = []
naluno = 0
while True:
    dados.append(naluno)
    dados.append(str(input("Digite o nome do aluno: ")))
    dados.append(int(input("Digite a sua primeira nota: ")))
    dados.append(int(input("Digite a sua segunda nota: ")))
    aluno.append(dados[:])
    dados.clear()
    naluno += 1
    q = str(input("Quer cadastrar outro aluno? [S/N]")).upper()
    while q not in 'sSNn':
        print("Digite 'S' ou 'N' sua mula!")
        q = str(input("Quer cadastrar outro aluno? [S/N]")).upper()
    if q == 'N':
        break
print(f'{"N":<10}{"Nome":^10}{"Média":>10}')
print("**"*15)
for naluno, nome, nota1, nota2 in aluno:
    print(f'{naluno:<10} {nome:^10}{(nota1+nota2)/2:>10}')
print("**"*15)
m = 0
while True:
    m = int(input("Digite o número do aluno para ver as notas(Digite 999 para sair): "))
    if m == 999:
        break
    print(f'As notas do aluno {aluno[m][1]} foram: {aluno[m][2]} e {aluno[m][3]}')



