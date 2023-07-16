def find(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve algum erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')