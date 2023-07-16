"""Leia o primeiro termo e a razão e faça uma P.A de 10 termos"""

n1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite qual a razão dessa P.A: "))
décimo = n1 + (10 - 1) * r
print("A P.A ficou assim: ")
for c in range(n1, décimo + r, r):
    print(c, end=' → ')

print("\nGoodbye!")