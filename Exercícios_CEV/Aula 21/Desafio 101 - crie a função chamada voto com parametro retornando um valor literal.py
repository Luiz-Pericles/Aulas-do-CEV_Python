"""Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""


def voto(a):
    import datetime
    ano_atual = datetime.date.today()
    idade = ano_atual.year - a
    if 18 <= idade <= 65:
        print(f'Com {idade} anos: Voto obrigatório!')
    elif idade < 18:
        print(f'Com {idade} anos: Voto negado!')
    elif idade > 65:
        print(f'Com {idade} anos: Voto opcional.')


ano_nasc = int(input('Digite o seu ano de nascimento: '))
print("-=" * 30)
voto(ano_nasc)
