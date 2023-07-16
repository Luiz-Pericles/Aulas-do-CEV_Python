'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
-A média de idade do grupo;
-Qual é o nome do homem mais velho;
-Quantas mulheres têm menos de 20 anos.'''

lista1 = []
lista2 = []
lista3 = 0
contador = 0
for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    lista3 += idade
    sexo = str(input('Sexo, digite a tecla h para homem ou digite a tecla m para mulher ')).lower()
    if sexo == 'h':
        lista1.append(nome)
        lista2.append(idade)
    elif sexo == 'm' and idade < 20:
        contador = contador + 1


print(f'A média de idade do grupo é: {lista3/4}')
print(f'O homem mais velho é {lista1[lista2.index(max(lista2))]}, e a sua idade é {max(lista2)} anos')
print(f'{contador} mulher(es) possuem menos de 20 anos')
