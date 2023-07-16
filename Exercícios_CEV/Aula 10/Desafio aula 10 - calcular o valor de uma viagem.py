#Programa para calcular o valor a pagar de uma viagem, caso essa viagem passe
#de 200km, o usuário tem que pagar 0.45 por km, caso não, 0.5
distancia = float(input('Qual a distância dessa viagem em km? '))
if distancia > 200:
    print(f'O preço da passagem é R${distancia*0.45}')
else:
    print(f'O preço da passagem para viagens menores é R${distancia*0.5}')

print('Tenha uma boa viagem!')