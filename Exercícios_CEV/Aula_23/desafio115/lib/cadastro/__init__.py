def user_option():
    from time import sleep
    while True:
        sleep(1.5)
        try:
            option = int(input('\nDigite uma opção:\n[1]-Cadastrar um usuário\n[2]-Ver usuários cadastrados'
                               '\n[3]-Sair do sistema de cadastro.\n--> '))
        except(ValueError, TypeError):
            print('\033[31mVocê digitou uma opção inválida!\033[m')
            continue
        else:
            if 3 >= option >= 1:
                return option
            else:
                print('\033[31mVocê digitou um número inteiro inválido!\033[m')
                continue


def title(msg, tam=45):
    if len(msg) > tam:
        tam = len(msg)
    print('-' * tam)
    print(msg.center(45))
    print('-' * tam)


def ler(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro na leitura do arquivo!')
    else:
        title('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def register(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

