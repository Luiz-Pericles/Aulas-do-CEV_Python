'''DESAFIO 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')), int(input('Digite o último valor: ')),)
print(f'Os valores digitados foram: {tupla}')
print(f'A) Apareceu o número 9 no total de {tupla.count(9)} vez')
if 3 not in tupla:
    print('B) Não foi digitado o valor 3')
else:
    print(f'B) Na posição {tupla.index(3)} foi digitado o valor 3')
print(f'C) Os números pares digitados foram: ', end=(' '))
for numeros in tupla:
    if numeros % 2 == 0:
        print(numeros, end=('  '))