"""Desafio 115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from lib.cadastro import *
from lib.arquivo import *


arq = 'cadastro_de_pessoas.txt'
if not find(arq):
    create(arq)

#Boas vindas do sistema:
title('Bem-vindo ao primeiro sistema de cadastro feito por Luiz Péricles!')
while True:
    n = user_option()
    if  n == 1:
        #Cadastra um usuário no arquivo.
        title('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        register(arq, nome, idade)
    elif n == 2:
        #Mostra os usuários cadastrados no arquivo.
        ler(arq)
    elif n == 3:
        title('Sistema sendo finalizado... Até logo!')
        break