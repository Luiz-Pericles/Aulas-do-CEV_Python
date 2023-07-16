'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1.000,00
c) Qual é o nome do produto mais barato.'''
print('-='*15)
print("It's Shop Time!")
print('-='*15)

namelist = []
pricelist = []
c = 0
while True:
    name = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço desse produto: R$ '))
    namelist.append(name)
    pricelist.append(price)
    if price > 1000:
        c += 1
    option = str(input('Quer cadastrar outro produto? [S/N]: ')).upper()
    while option not in 'SN':
        option = str(input('Quer cadastrar outro produto? [S/N]: ')).upper()
    if option == 'S':
        continue
    elif option == 'N':
        break
print(f'a) O total gasto foi de R$ {round(sum(pricelist),2)}')
print(f'b) {c} produto(s) custam mais de R$ 1.000,00')
cheap = pricelist.index(min(pricelist))
print(f'c) O nome do produto mais barato é {namelist[cheap]}')
