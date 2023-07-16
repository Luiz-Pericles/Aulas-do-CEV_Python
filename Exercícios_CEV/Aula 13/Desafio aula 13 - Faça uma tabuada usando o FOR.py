"""Refazendo o desafio de n 09 do curso em vídeo, em que ele pedia para fazer uma tabuada, porém foi utilizado vários
comando de print, agora é para refazer o código de forma simples."""

numero = int(input("Digite um número: "))
print("Segue a tabuada desse número: ")
for c in range(0, 11):
    print(f"{numero} x {c} = {numero * c}")

print("Fim!")
