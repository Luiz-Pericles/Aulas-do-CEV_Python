#Nesta aula são os vistos os dicionários que servem para nomear os indexadores de uma lista.
"""Para utilizar essa função é necessário declarar uma variável que vai ser o dicionário e colocar essa variável para
receber os valores entre chaves, por exemplo: """
'''filme = {'titulo':'star wars', 'ano':1977, 'diretor':'George'}
print(filme.values())
print(filme.keys())
print(filme.items())
print(filme)
for k,v in filme.items():
    print(f'O {k} é {v}')'''

#Como adicionar um dicionário dentro de uma lista:
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade'
                             ' Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for k in e.values():
        print(f'{k}', end=' ')

