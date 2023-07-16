"""Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado"""
#Mensagens de boas vindas:
print('\033[;30;42m=\033[m'*60)
print('\033[1;32;40mOlá! Seja bem-vindo ao LUIZ BANK LTDA.                      \033[m')
print('\033[;30;42m=\033[m'*60)

#Aqui são os inputs para pegar informações:
casa = float(input('Informe qual o valor do imóvel que deseja adquirir: '))
tempo = int(input('Diga-me em quantos meses deseja pagar esse bem? '))
salário = float(input('Agora, me informe o seu salário: '))


#Cálculo do valor da parcela da casa:
parcelas = casa / tempo

#Condicional para saber se o valor das parcelas é maior que 30% de seu salário:
if parcelas > salário*0.3:
    print(f'Financiamento negado! O valor da parcela ficaria: R${parcelas}')
else:
    print(f'O valor das parcelas do seu imóvel será: R${round(parcelas,2)}')
    aceite = input('Deseja continuar a compra?\n responda "s" ou "n": ')
#Condicional dentro de condicional para o usuário informar se aceitará a proposta.
    if aceite == 's':
        print('\nAgora você é um novo cliente da LUIZ BANK LTDA.')

print('Tenha um ótimo dia!')








