"""Desafio 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
cadastro = dict()
cadastro['nome'] = str(input('Digite seu nome: '))
cadastro['nascimento'] = int(input('Digite seu ano de nascimento: '))
cadastro['ctps'] = int(input('Digite o número de sua CTPS(digite 0 caso não tenha): '))
if cadastro['ctps'] != 0:
    cadastro['salário'] = float(input('Digite seu salário: '))
    cadastro['contratação'] = int(input('Digite o ano de sua contratação: '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - cadastro['nascimento']
print(cadastro)
for k, v in cadastro.items():
    print(f'O {k} corresponde a {v}')
