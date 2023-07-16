"""Desafio 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários."""


'''def leiaDinheiro(msg):
    valor = str(input(msg)).replace(',','.').strip()
    while True:
        if valor.isalpha() or valor == '':
            print(f'Erro! {valor} não é um número válido.')
            valor = str(input(msg)).replace(',','.').strip()
        else:
            return float(valor)'''

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.count('.') == 1 and len(entrada) > 1 and entrada.find('.')!=0 and entrada.replace('.', '0').isnumeric():
            válido = True
            return float(entrada)
        elif entrada.isnumeric():
            válido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')




