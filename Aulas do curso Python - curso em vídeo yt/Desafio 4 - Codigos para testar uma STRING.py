#Ainda não entendi bem como funciona o 'isalpha', porque quando coloco mais de uma palavra
#ele identifica como falso, e também não sei como é o ISTITLE, ISPRINTABLE

nome = input('Digite qualquer coisa: ')
print('É um número?', nome.isnumeric())
print('É uma letra?', nome.isalpha())
print('Está tudo em minúsculo?', nome.islower())
print('Está em decimal?', nome.isdecimal())
print('É um título?', nome.istitle())
print('Isso é impresso?', nome.isprintable())
print('Essa porra é alfanúmerica?', nome.isalnum())
