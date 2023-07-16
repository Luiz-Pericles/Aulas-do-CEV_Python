#Como utilizar o *Interactive*, *Help*, *docstrings*, *Argumentos opcionais*,
#*escopo de variáveis*, *funções que retornam resultados*.
"""O HELP() é utilizado quando se tem uma dúvida sobre a função, aí você digita o exemplo: help(print) para mais
informações e o comando help vai mostrar o manual da função *print*"""
"""As DOCSSTRINGS são um resumo da função que o criador colocou para dar um norte ao usuário que irá utilizar a função
e ao utilizar a função help() esse tutorial fica a amostra para o usuário, como exemplo:"""
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)

"""ARGUMENTOS OPCIONAIS é basicamente ao criar uma função com def caso o usuário digite menos parâmetros do que é 
solicitado a função vai aceitar, porque inicialmente vamos atribuir um valor para esse parâmetro como exemplo:
def somar(a = 0, b = 0, c = 0):
    c = a + b + c
    print(c)
#main function:
somar(2,5)
#Vai retornar o valor 7 sem dá erro"""


"""ESCOPO DE VARIÁVEIS é o local onde uma variável vai existir ou o local onde uma variável não vai existir.
Em resumo: se você declarar uma variável em uma DEF e tentar informar essa variável declarada na main function vai dar
erro, pois a variável declarada só existe dentro do erro, exemplo de ERRO a seguir:"""

"""def teste():
    x = 8
    print(f"A váriável x vale {x}")
    print(f"A variável n vale {n}")
#Main:
n = 2
print(f"A váriável x vale {x}")
print(f"A variável n vale {n}")"""

"""Assim podemos dizer que a variável n é uma variável GLOBAL e a variável x é uma variável local."""
#Teste capirotado com escopos de variáveis:

"""
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#Main:
a = 5
teste(a)
print(f'A fora vale {a}')"""

"""RETORNADO VALORES, utilizando a função RETURN é possível atribuir o valor de retorno da função a uma variável, segue
exemplo de como ficaria: """
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
#Main:
r1 = somar(3, 4, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os valores valem {r1}, {r2}, {r3}')
