'''Desafio 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respecitvos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
tupla = ('Biscoito', 4, 'farinha', 2, 'Maça', 1, 'Xampu', 12, 'Suco', 5,
         'Donuts', 4, 'Banana', 3, 'Camarão', 26, 'Queijo', 30, 'Tomate', 4)
print('-=' * 20)
print(f'{"LISTA DE SUPERMERCADO":^40}')
print('-=' * 20)
for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end=(''))
    elif c % 2 == 1:
        print(f'R${tupla[c]:>6.2f}')
