'''Cadeia de caracteres = string ou STR'''
'''Para o exemplo de str( frase = Curso em vídeo Python)'''
#print(frase[9]) --> Identifica o 9° caracter e imprime na tela.
#print(frase[9:13] --> Identifica do 9° ao 13° caracter e imprime na tela.
#print(frase[9:21:2] --> Identifica do 9 ao 13° caracter e imprime pulando de dois em dois.
#print(frase.find('em')) --> Ele mostra em qual caracter iniciou a palavra/frase buscada.
#print('Curso' in frase) -- > Ele mostra True se existe essa frase e False, caso não existisse.
#print(frase.replace('Python','Android')) --> Ele imprime o objeto frase, substituindo o 'Python' por 'Android'.
#print(frase.upper()) --> Deixa a string tudo em MAIÚSCULO.
#print(frase.lower()) --> Deixa a string tudo em minúsculo.
#print(frase.capitalize()) --> Deixa a primeira letra da string em maiuscúlo e o restante em minúsculo.
#print(frase.title()) --> Análise quantas palavras de acordo com ESPAÇOS e deixa a primeira letra maiuscúlo de cada palavra.
#print(frase.strip()) --> Remove os ESPAÇOS inúteis da string que são os espaços do ínicio e do fim, então se a string tivesse espaço no ínicio ele seria removido.
#print(frase.rstrip()) --> Remove os ESPAÇOS da direta.
#print(frase.lstrip()) --> Remove os ESPAÇOS da esquerda.
#print(frase.split()) --> Separa a string em uma lista, ele separa a partir dos espaços, então cada palavra vira um elemento da lista.

frase = 'Curso em vídeo Python'
print(frase.find('em'))





