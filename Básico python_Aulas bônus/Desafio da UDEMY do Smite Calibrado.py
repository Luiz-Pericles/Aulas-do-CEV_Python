"""Em um banco, para se cadastrar uma conta bancária, é necessário informar o número da conta, o nome do titular da conta
e o valor de depósito inicial que o titular depositou ao abrir a conta. Este valor de depósito inicial, entretanto, é
opcional, ou seja: se o titular não tiver dinheiro a depositar no momento de abrir sua conta, o depósito inicial não
será feito e o saldo inicial da conta será, naturalmente, zero.

Importante: uma vez que uma conta bancária for aberta, o número da conta nunca poderá ser alterado. Já o nome do titular
pode ser alterado (pois uma pessoa pode mudar de nome por ocasião de casamente, por exemplo).

Por fim, o saldo da conta não pode ser alterado livremente. É preciso haver um mecanismo para proteger isso. O saldo só
aumenta por meio de depósitos, e só diminui por meio de saques. Para cada saque realizado, o banco cobra uma taxa de $5.
Nota: a conta pode ficar com saldo negativo se o saldo não for suficiente para realizar o saque e/ou pagar a taxa.

Você deve fazer um programa que realize o cadastro de uma conta, dando opção para que seja ou não informado o valor de
depósito inicial. Em seguira, realizar um depósito e depois um saque, sempre mostrando os dados da conta após cada operação."""

import time

print('\033[;30;42m=\033[m'*30)
print(f'\033[1;32;40mBoas-vindas ao LUIZ BANK LTDA.\033[m\n\033[1;32;40mNosso prazer é roubar você :) \033[m')
print('\033[;30;42m=\033[m'*30)
nconta = (int(input('Para realizar o seu cadastro, favor informar o n°(apenas números) da sua conta: ')))
nometitular = str(input('Favor informar o seu nome para cadastro do titular: '))
deposito_inicial = str(input('Deseja realizar um depósito inicial para abertura de conta? [S/N] '))
if deposito_inicial in 'Ss' :
    valor_inicial = float(input('Informe o valor inicial do deposito: R$ '))
elif deposito_inicial.upper() == 'N':
    valor_inicial = 0
print("--"*35)
print(f'Parabéns {nometitular}, agora você é um novo cliente da LUIZ BANK LTDA.')
print(f'O número de sua conta é {nconta} e o seu saldo atual é de R${valor_inicial}')
print("--"*35)
time.sleep(4)
saldo = valor_inicial
while True:
    print()
    op = str(input('Digite a operação desejada:\n1-[SAQUE]\n2-[DEPOSITAR]\n3-[Sair]\n-->'))
    if op == '3':
        break
    if op == '1':
        print(f'OBS: Para saques o banco cobra uma tarifa de R$ 5.00')
        saque = float(input(f'Valor disponível para saque: R$ {saldo}\nDigite o valor que deseja sacar: R$ '))
        saldo = saldo - saque - 5
    if op == '2':
        deposito = float(input(f'Saldo atual: R${saldo}.\nDigite o valor o qual deseja depositar: R$ '))
        saldo += deposito
    print(f'{nometitular}, o seu saldo bancário após a operação é de \033[7;34;40mR${saldo}\033[m')
    time.sleep(2)
print('-='*25)
print(f'O banco LUIZ BANK LTDA. agradece a preferência, volte sempre!')


