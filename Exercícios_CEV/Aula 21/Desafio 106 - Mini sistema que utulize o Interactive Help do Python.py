"""Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se
encerrará.
OBS: use cores."""


def ajuda():
    """
    Digite qualquer built-in function do Python para mais informações.
    :return: Retorna a função que você digitou!
    """
    from time import sleep
    while True:
        msg = str(input('Função ou biblioteca --> '))
        if msg.upper() == 'FIM':
            print('\033[7;30;41mGoodbye!\033[m')
            break
        else:
            print("\033[7;34;40m=-" * 30)
            print('     Analisando a função...')
            print("=-" * 30)
            print("\033[m")
            sleep(2)
            print("\033[7;32;40m")
            help(msg)
            print("\033[m")


help(ajuda)
ajuda()
