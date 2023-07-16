"""ABAIXO ESTÁ O CÓDIGO PARA SORTEAR UM NOME DE UMA LISTA:
import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print(f"O aluno sorteado foi: {sorteio}")"""

#Para sortear uma lista e mostrar todos na ordem embaralhada:
import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f"A ordem embaralhada dos alunos é: {lista}")