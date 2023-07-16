import math
angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O seno desse ângulo é: {seno}\n"
      f"o cosseno é: {cosseno}\n "
      f"a tangete é: {tangente}")