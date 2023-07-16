# Esse é o desafio para escrever o valor da hipotenusa de um triangulo retângulo,
#a partir da digitação dos catetos.
import math
oposto = int(input("Digite o cateto oposto: "))
adjacente = int(input("Digite o cateto adjacente: "))

hipotenusa = pow(oposto,2) + pow(adjacente,2)

print(math.sqrt(hipotenusa))
