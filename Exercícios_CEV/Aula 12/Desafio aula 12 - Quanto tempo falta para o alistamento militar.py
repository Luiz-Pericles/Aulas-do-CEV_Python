'''Faça um programa que leia o ano de nascimento de um jovem e informe
,de acordo com idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora dele se alistar
-Se já passou do tempo de ele se alistar
Seu programa também deve mostrar o tempo que falta ou o prazo que passou.'''
ano = int(input('Em que ano o sr. nasceu? '))
idade = 2023 - ano
if idade == 18:
    print('Está na hora do sr. se alistar no serviço militar!')
elif idade > 18:
    prazo = idade - 18
    print(f'Já passou o prazo do sr. se alistar no serviço militar!')
    print(f'\n\033[1;32;40mO sr. deveria ter se alistado há {prazo} anos\033[m')
elif idade < 18:
    prazo = 18 - idade
    print('Ainda não é o tempo do sr. se alistar')
    print(f'\n Faltam {prazo} ano(s) para o sr. se alistar!')
