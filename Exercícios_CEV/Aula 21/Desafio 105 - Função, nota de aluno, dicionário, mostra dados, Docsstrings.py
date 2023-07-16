"""Desafio 105:  faça um programa que tenha uma função notas() que pode receber vários notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função."""

def notas(*n, sit=False):
    """
    Essa função mostra o resultado das notas inseridas no sistema.
    :param n: É a variável que recebe as notas dos alunos
    :param sit: É para mostrar a situação do aluno se já dentro da média
    :return: Retorna o dicionário com a situação do aluno.
    """
    sit_aluno = dict()
    sit_aluno['Total de notas'] = len(n)
    sit_aluno['maior nota'] = max(n)
    sit_aluno['menor nota'] = min(n)
    soma = 0
    for c in n:
        soma += c
    media = soma / len(n)
    sit_aluno['média das notas'] = round(media,2)
    if sit:
        if media >= 7:
            sit_aluno['situação'] = 'Aprovado'
        else:
            sit_aluno['situação'] = 'Reprovado'
    return sit_aluno


resp = notas(3.5, 4, 5, 5, sit=True)
print(resp)
help(notas)