#Aula de listas parte 2 -->
#No ínicio da aula do Guanabara é visto que possível colocar uma lista dentro de uma lista são chamadas de LISTAS
#COMPOSTAS, segue o exemplo a seguir: """
'''dados = []
dados.append(input("Digite: "))
numeros = list()
numeros.append(dados[:])
print(numeros)'''
#Para referenciar uma lista dentro de uma lista funciona assim:
pessoas = [['pedro', 25], ['maria', 19], ['joão', 32]]
#Para printar 'maria', 'joao' e '25' respectivamente:
print(pessoas[1][0])
print(pessoas[2][0])
print(pessoas[0][1])