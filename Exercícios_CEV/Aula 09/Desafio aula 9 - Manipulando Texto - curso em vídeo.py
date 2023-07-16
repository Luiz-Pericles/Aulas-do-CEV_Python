'''Crie um programa que leia o nome de uma
pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: '))
print(f'Bem vindo {nome}!')
upper = nome.upper()
lower = nome.lower()
length = len(nome.replace(" ", ""))
lista = nome.split()
length1 = len(lista[0])
primeiro = lista[0]
print(f'''O nome Maiúsculo é: {upper} 
O nome Minúsculo é: {lower}
Há essa quantidade de letras: {length}
Há essa quantidade de letras no primeiro nome: {length1} ''')

