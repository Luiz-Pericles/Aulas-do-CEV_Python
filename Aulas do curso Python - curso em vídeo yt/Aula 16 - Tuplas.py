#Essa aula é a abertura do 3º mundo
'''No íncio da aula é dito que iremos ver: estruturas compostas(variáveis compostas), rotinas, tratamento de erro.'''
'''Aula 16 - Variáveis compostas(TUPLAS, LISTAS e DICIONÁRIOS)'''
#Basicamente, a variável simples é aquela que é apenas atribuída um valor, diferente da variável composta.
'''As tuplas são variáveis que você pode escolher quantos valores quer atribuir nessa variável'''
#As TUPLAS são imutáveis, logo não há como substituir um valor da tupla por outro.
#Exemplos de tuplas, obs: pode vir entre parênteses ou sem:
'''lanche = ('suco', 'hambuguer', 'pudim')
print(lanche)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demaize!')'''

#Mostrando as tuplas de outa forma:
'''lanche = ('suco', 'hambuguer', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')'''
#ou
'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''
#ou
'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}'''
#Utilizando a função 'sorted()' é possível deixar a tupla organizada em ordem alfabética. Ex:
'''lanche = ('suco', 'hambuguer', 'pudim') 
print(sorted(lanche))'''
#É possível somar tuplas dessa forma:
'''a = (1, 4, 5, 8)
b = (3, 4, 6, 7)
c = a + b
d = b + a
print( c,'\n',d)
#Para contar quantas vezes um valor aparece em uma tupla utilize a função 'VARIAVEL.count()':
print(f'Conte quantas vezes aparece o nº 4: {c.count(4)}')
#Para saber em qual posição está um variável de uma tupla utilize a função 'VARIAVEL.index()':
print(f'O valor 7 está na posição {c.index(7)} e o segundo 4 está na posição {c.index(4, 2)}')'''
#Uma tupla pode ter uma string e um inteiro dentro dela. Ex:
'''tupla = ('Gustavo', 29, 'm')
print(tupla)'''
#Não é possível substituir dados de uma tupla, mas é possível apagar uma tupla. Ex: (vai da erro)
tupla = ('Gustavo', 29, 'm')
del(tupla)
print(tupla)