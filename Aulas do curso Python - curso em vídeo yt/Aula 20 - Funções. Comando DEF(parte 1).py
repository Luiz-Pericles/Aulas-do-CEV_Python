"""A função *def* vem com o principal papel de criar funções para deixar o código menos repetitivo e otimizado.
Segue um exemplo de como a função def pode ajudar o código ficar mais limpo:"""
#Sem o def:
"""print('-=' * 30)
print('Exemplo do Gustavo Guanabra')
print('-=' * 30)"""""
#Com o def:
"""def mostralinha(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)

#Main function:
mostralinha('Exemplo do Gustavo Guanabara')"""
#Exemplo de como criar uma função de soma com def:
"""def soma(a, b):
    print(f"A = {a} e B = {b}")
    c = a + b
    print(f"A soma de A + B = {c}")

#Main function:
soma(3, 4)"""
#Melhorando a função de soma, para somar independente do limite de variáveis utilizando um EMPACOTADOR de PARÂMETROS( * ):
def contador(* núm):
    print(sum(núm))

#main funcition:
contador(3, 4, 5)
contador(2, 2)
contador(9, 8, 5, 2, 1)
#Dobrando cada valor e uma lista com def:
"""def dobra(lista):
    stop = 0
    while stop < len(lista):
        print(lista[stop] * 2)
        stop += 1

números = [3, 5, 7, 10]
dobra(números)"""

