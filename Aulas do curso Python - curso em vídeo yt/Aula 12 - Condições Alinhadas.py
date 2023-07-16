#Nesta aula foi visto a estrutura condicional parte 2
#Foi apresentado a função "elif"
#Basicamente serve para aumentar as condições do "if"

nome = str(input('Digite seu nome: '))
c = nome.lower()
if c == 'luiz':
    print(f'Que belo nome você tem, {nome.title()}!')
elif c == 'maria' or c == 'joão':
    print(f'Seu nome é bem comum, {nome}')
else:
    print(f'Seu nome é bem normal')
print(f'Prazer em lhe conhecer {nome}!')