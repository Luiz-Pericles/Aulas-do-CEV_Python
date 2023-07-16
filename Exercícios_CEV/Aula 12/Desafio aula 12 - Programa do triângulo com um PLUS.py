'''Leia três comprimentos e informe se pode formar um triângulo, e também,
caso forme um triângulo informe se é um:
- Triângulo equilátero: todos os lados iguais;
- Triângulo isóceles: dois lados iguais;
- Triângulo Escaleno: todos lados diferentes.'''
l1 = float(input('Digite o primeiro comprimento: '))
l2 = float(input('Digite o segundo comprimento: '))
l3 = float(input('Digite o terceiro comprimento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and  l3 < l1 + l2:
    print('Esses lados formam um triângulo!')
    if l1 == l2 and l2 == l3:
        print('\nE é um triângulo equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('\nÉ um triângulo isóceles')
    else:
        print('\nÉ um triângulo escaleno!')
else:
    print('Esses lados não formam um triangulo')