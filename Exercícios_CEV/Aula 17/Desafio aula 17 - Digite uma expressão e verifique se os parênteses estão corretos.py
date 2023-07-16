"""Desafio 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""
ex = str(input("Digite a expressão: "))
c1 = []
for c in ex:
    if c == '(':
        c1.append(c)
    elif c == ')':
        if len(c1) > 0:
            c1.pop()
        else:
            c1.append(c)

if len(c1) == 0:
    print('A sua expressão está correta!')
else:
    print('Sua expressão está escrita de forma errada!')
print('Goodbye!')