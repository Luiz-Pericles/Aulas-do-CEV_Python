'''Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços'''

#Método com o FOR -->
frase = str(input('Digite a sua palavra/frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ""
for letra in range (len(junto)-1,-1,-1):
     inverso += junto[letra]
print(f'Frase normal: {junto}')
print(f'Frase inversa: {inverso}')
if junto == inverso:
    print('São Polindromos!')
else:
    print('Não são Polindromos!')


#Ou podemos criar com o método de fatiamento -->
'''frase = str(input('Digite a sua palavra/frase: ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]

print(f'Frase normal: {junto}')
print(f'Frase inversa: {inverso}')
if junto == inverso:
    print('São Polindromos!')
else:
    print('Não são Polindromos!')'''