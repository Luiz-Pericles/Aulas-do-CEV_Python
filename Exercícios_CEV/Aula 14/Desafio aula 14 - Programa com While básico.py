"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto. """

sexo = str(input('Digite: \nm[Mulher] ou h[Homem]\n')).strip().lower()[0]
while sexo != 'm' and sexo != 'h':
    print('Você digitou a tecla errada, digite novamente.')
    sexo = str(input('Digite: \nm[Mulher] ou h[Homem]')).lower()
print('Você digitou o valor correto, goodbye!')
