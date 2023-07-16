'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''
nota1 = float(input('Digite a sua primeira nota de 0 a 10: '))
nota2 = float(input('Digite a sua segunda nota de 0 a 10: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print('APROVADO(A)!')
elif média > 5 and média < 7:
    print('RECUPERAÇÃO!')
elif média <= 5:
    print('REPROVADO(A)!')
print(f'Sua média foi: {round(média,2)}')