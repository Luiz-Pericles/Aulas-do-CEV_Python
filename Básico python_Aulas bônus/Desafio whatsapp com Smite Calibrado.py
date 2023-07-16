"""Faça um programa para ler a cotação do dólar, e depois um valor em dólares a ser comprado por uma pessoa em reais.
Informar quantos reais a pessoa vai pagar pelos dólares, considerando ainda que a pessoa terá que pagar 6% de IOF sobre
o valor em dólar. Criar uma classe CurrencyConverter para ser responsável pelos cálculos."""
import time

print('\033[;30;42m=\033[m'*40)
print('\033[1;32;40mBem-vindo a empresa LUIZ CURRENCY LTDA. \033[m')
print('\033[;30;42m=\033[m'*40)
cotação = {'dólar': 5.00, 'seu pai' : 999.00}
print(f'Segue a lista do preço das moedas na cotação imaginária de hoje:')
print('-'*70)
print(f'Taxa de 5% IOF sobre cada transação\n')
print(f"{'MOEDA':^10}{'PREÇO':>10}")
for k, v  in cotação.items():
    print(f"{k:^10}{v:>10}")
time.sleep(4)
print()
while True:
    op = str(input('Digite qual moeda deseja comprar:\n[1]-dólar\n[2]-seu pai\n[3]-Sair\n--> '))
    if op == '1':
        valor = float(input('Quantos dólares você quer comprar: $ '))
        conversão = (valor*5)
        iof = 1.06
        cambio = conversão * iof
        print(f'Para comprar ${valor} dólares, você vai precisar pagar \033[7;34;40mR${cambio} em reais\033[m')


    if op == '2':
        valor = float(input('Quantos pais você quer comprar: Pai($) '))
        conversão = (valor*999)
        iof = 1.06
        cambio = conversão * iof
        print(f'Para comprar ($){valor} pais, você vai precisar pagar \033[7;34;40mR${cambio} em reais\033[m')

    if op == '3':
        break
print(f'A corretora LUIZ CURRENCY LTDA. agradece a preferência, volte sempre!')



