""""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. (Dica: use o modulo time e função sleep
que faz o Python aguardar antes de executar o próxima comando)."""
import time
print("\033[1;34;40m10 seconds left for the NEW YEAR!\033[m")
for c in range(10, 0, -1):
    print(f"{c}...")
    time.sleep(1)
print("HAPPY NEW YEAR!")
