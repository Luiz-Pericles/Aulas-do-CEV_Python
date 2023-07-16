'''ORDEM DE PRECEDÊNCIA DOS OPERADORES PYTHOM 1° LUGAR É OS PARENTÊSES (),
2° LUGAR É A POTÊNCIA QUE É REPRESENTADO POR **, 3 TERCEIRO LUGAR É MULTIPLICAÇÃO *,
 DIVISÃO /, DIVISÃO INTEIRA //, e RESTO DA DIVISÃO %, em 4° Lugar é a soma + e a subtração -'''

#Desafio 5: a seguir, faça um programa que leia um número inteiro e faça seu succesor e antecessor
#numero = int(input('Digite um número e mostratei o succesor e antecessor: '))
#print(f'Esse é o sucessor {numero+1} e esse é o antecessor {numero-1}')

#Desafio 7: faça um programa que pegue as notas de um aluno e calcule a média
#n1 = float(input('Digite a primeira nota do aluno: '))
#n2 = float(input('Digite a segunda nota do aluno: '))
#print(f'A média desse aluno foi {(n1+n2)/2}')

#Desafio 9: Escreva um número inteiro e faça sua tabuada
#n = int(input('Digite um número inteiro: '))
#print(f'Essa é a tabuada desse número: \n{n}+1: {n+1} \n{n}+2: {n+2}' )

#Desafio 10: Crie um programa que leia quanto dinheiro a pessoa tem e mostre em dolares
#dinheiro = float(input('Quanto de dinheiro você tem? '))
#print(f'Com essa grana você tem {dinheiro * 4.95} dólares')

#desafio 11: Faça um programa que calcule a área de sua parede e calcule quanto de tinta
#será gasto para pintar a parede
#altura = float(input('Qual é a altura de sua parede? '))
#largura = float(input('Qual é a largura de sua prede? '))
#area = largura * altura
#print(f'Sua parede tem {area}m² de área, considerando que para cada 2m² é usado 1 litro de tinta.')
#print(f'Então vai ser necessário {area/2} de litros de tinta pra pintar sua parede')

while True:
    nome = input("Digite o seu nome: ")
    if nome.isalpha():
        break
    else:
        print("Erro! Nomes não devem conter dígitos.")

print(f"\nBem Vindo!, {nome}\n")

salario = float(input("Poderia me fornecer seu salário para aplicarmos o seu aumento: "))
aumento = 15

novo_salario = salario + (salario * aumento / 100)

print(f"Muito bem, aqui está o seu salário com aumento aplicado: R${novo_salario:.2f}")