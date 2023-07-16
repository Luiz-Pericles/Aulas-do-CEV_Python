#Esse é um programa para ler a velocidade de um carro e informar se o mesmo
#Estava acima velocidade, caso sim, ele aplica uma multa 7 reais para km ultrapassado.

velocidade = float(input('Informe a velocidade do veículo: '))
vpermitida = 80
multa = float(velocidade - vpermitida)
if velocidade > vpermitida:
    print('Você ultrapassou a velocidade permitida!')
    print(f'O valor da multa é R${multa*7}')
else:
    print('Muito bem, continue sua viagem!')