#Listas são mutáveis, isso é, podemos colocar novos valores, retirar e alocar em uma lista.
#insert, insere valores em uma posição de uma lista, Utilizando:
'''lista = ['suco', 'feijoada', 'presunto']
lista.insert(0, 'treloso')
print(lista)'''
#append, adiciona valores em uma lista, Utilizando:
'''lista = []
n = 0
for c in range(0,10):
    n = n + 2
    lista.append(n)
print(lista)'''
#del ou pop, removem valores de uma lista a partir de uma posição, utilizando:
'''lista = ['treloso', 'suco', 'feijoada', 'presunto']
del lista[2]
lista.pop(1)
print(lista)'''
#remove, remove valor de uma lista de acordo com o nome, utlizando:
'''lista = ['treloso', 'suco', 'feijoada', 'presunto']
lista.remove('feijoada')
print(lista)'''
#lista, a partir de uma variável, cria uma lista, utilizando:
'''valores = list(range(11,4, -1))
print(valores)
valores.sort()
print(f'Na ordem: {valores}')
valores.sort(reverse=True)
print(f'Fora de ordem novamente: {valores}')'''
#len, para saber o tamanho de uma lista, utilizando:
'''lista = (1, 'joao', 2, 3, 4, 5)
print(len(lista))'''
#enumerete, para saber a posição de um valor na lista, combine com for, utilizando:
'''lista = [3, 'maria', 21]
for c, v in enumerate(lista):
    print(f'O valor {v} está na posição {c}ª da lista.')'''
#Para criar uma ligação de uma lista com a outra basta igualar, verifique q a edição de uma lista, edita a outra:
'''a = [2, 3, 4, 7]
b = a
b[2] = 8
print(b)
print(a)'''
#Para criar uma cópia de uma lista com outra, faça o seguinte:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(b)
print(a)