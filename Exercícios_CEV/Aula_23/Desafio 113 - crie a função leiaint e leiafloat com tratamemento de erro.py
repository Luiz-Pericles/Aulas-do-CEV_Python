""""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(msg):
    while True:
        try:
            int(input(msg))
        except (ValueError, TypeError):
            print('Você provavelmente digitou um valor estranho!')
        else:
            break


def leiaFloat(msg):
    while True:
        try:
            float(input(msg))
        except (ValueError, TypeError):
            print('Confira o valor digitado e tente novamente!')
        else:
            break


leiaInt('Digite um número inteiro: ')
leiaFloat('Digite um número real: ')
