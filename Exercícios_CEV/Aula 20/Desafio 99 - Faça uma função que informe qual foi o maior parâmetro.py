"""Desafio 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def maior(* núm):
    if len(núm) == 0:
        print("-=" * 30)
        print("Analisando os valores passados...")
        print(f"Foram informados {len(núm)} valores ao todo.")
        print("Não há maior número, considere que é 0")
    else:
        print("-=" * 30)
        print("Analisando os valores passados...")
        print(f"{núm} Foram informados {len(núm)} valores ao todo.", flush=True)
        print(f"O maior valor digitado foi {max(núm)}.")



#Main function:
maior(2, 0, 6, 33, 1)
maior(1, 1, 1)
maior(0, 0)
maior(5)
maior()
