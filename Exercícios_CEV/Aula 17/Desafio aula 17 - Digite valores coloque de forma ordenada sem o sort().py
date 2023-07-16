"""Desafio: 80. Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na
posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela."""
print('Bem-vindo, nesse programa irei ordenar os valores digitados!')
print('Digite 5 números')
listanum = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > listanum[len(listanum)-1]:
        listanum.append(n)
    else:
        pos = 0
        while pos < c:
            if n <= listanum[pos]:
                listanum.insert(pos, n)
                break
            pos += 1


print(listanum)


