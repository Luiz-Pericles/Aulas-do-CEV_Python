#Nesta aula, veremos a estrutura de repeticão
#Exemplos abaixo:
"""for c in range(0, 10):
    print(c)
print("FIM!")"""

"""for c in range(0, 10, 2):
    print(c)
print("Fim!")"""

"""for c in range(10, 0, -1):
    print(c)
print("Fim!")"""

"""n = int(input("Digite um número: "))
for c in range(0, n):
    print(c)
print("Fim!")"""

"""i = int(input("Ínicio: "))
f = int(input("Fim: "))
p = int(input("Passos: "))
for c in range(i, f+1, p):
    print(c)
print("Fim!")"""

s = 0
for c in range(0,4):
    n = int(input("Digite um valor: "))
    s += n
print(f"O somatório de todos os valores foi: {s}")

