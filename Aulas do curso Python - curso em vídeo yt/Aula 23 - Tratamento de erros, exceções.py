"""Erro sintático: um erro ao escrever errado uma função. Erro semântico: um erro de significado no programa, ao exemplo
solicitar para printar x, sendo que ele nunca foi definido antes."""
#Tratando Exceptions Error:
"""As funções ''try'' e ''except'' são obrigatórias, já a ''else'' e a ''finally'' são opcionais. E todo 'try' pode ter
mais de um except.

try: (OPERAÇÃO)
except: (FALHOU)
else: (Se deu certo) (OPERAÇÃO)
finally: (Se deu certou ou FALHOU, ele faz a operação de qualquer forma)"""


try:
    a = int(input('Numerador: '))
    b = int(input('Denomiador: '))
    r = a / b
except:
    print('Infelizmente algo deu errado :(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado.')


#Outras formas de tratamento de erros:
try:
    a = int(input('Numerador: '))
    b = int(input('Denomiador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__} ')
#Outras formas de tratamento de erros:
try:
    a = int(input('Numerador: '))
    b = int(input('Denomiador: '))
    r = a / b
except ZeroDivisionError:
    print(f'Não é possível realizar uma divisão por ZERO!')
except (ValueError, TypeError):
    print(F'Tivemos um problema com os tipos digitados.')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os números.')


