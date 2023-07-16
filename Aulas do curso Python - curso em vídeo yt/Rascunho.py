def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    return nome, idade

def mostrar_usuarios_cadastrados(usuarios):
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario[0]}, Idade: {usuario[1]}")

usuarios_cadastrados = []

while True:
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Sair do sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = cadastrar_usuario()
        usuarios_cadastrados.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        mostrar_usuarios_cadastrados(usuarios_cadastrados)

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")