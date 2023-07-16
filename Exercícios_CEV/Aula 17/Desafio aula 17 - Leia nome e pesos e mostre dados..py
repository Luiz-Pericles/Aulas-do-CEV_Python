"""Desafio 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
print("Welcome to the fatfobic program!")
print("-=" * 15)
pessoas = []
dados = []
mai = men = 0
digt = int(input("Quantas pessoas você quer cadastrar: "))
for c in range(0, digt):
	dados.append(str(input("Digite um nome: ")))
	dados.append(int(input("Digite um número: ")))
	if mai == men == 0:
		mai = dados[1]
		men = dados[1]
	elif dados[1] > mai:
		mai = dados[1]
	elif dados[1] < men:
		men = dados[1]
	pessoas.append(dados[:])
	dados.clear()
print(f'A) A quantidade de pessoas cadastradas foram {len(pessoas)}' )
print(f'B) A maior idade digitada foi: {mai}, da(s) pessoa(s): ', end="")
for nome, idade in pessoas:
	if idade == mai:
		print(f'[{nome}] ', end="")
print(f'\nC) A menor idade digitada foi: {men}, da(s) pessoa(s)', end="")
for nome, idade in pessoas:
	if idade == men:
		print(f'[{nome}] ', end="")
print("\nGoodbye!")
