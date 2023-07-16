#Para adicionar cor é necessário colocar o seguinte comando:
#'\033[X;Y;Zm'
#X é para o tipo de caracter, pode ser 0, 1, 4 ou 7.
#Y é a cor do texto vai do 30 a 37
#Z é a cor do Bacj vai de 40 a 47
print('\033[1;32;40mOlá mundo!\033[m')
print('Estou testando \033[1;34;40mos comandos\033[m de cores!')
print('\033[0;31mHá várias formas de colorir o texto')