#Nessa aula veremos a estrutura de repetição com teste lógico, a estrutura de repetição da aula 13, chama-se estrutura
#de repetição com variável de controle.

#COMPARATIVO FOR/WHILE -->
'''for c in range(1, 10):
    print(c, end=' ')
print('FIM!')

c = 1
while c < 10:
    print(c, end=' ')
    c = c + 1
print('FIM!')'''

#Método FLAG para parar a execução de um programa:
c = 1
while c != 0:
    c = int(input('Digite um valor: '))
print('FIM!')
