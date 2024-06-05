usuarioEsenha = {}
livros = {}

def carregar_dados():
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                usuario, senha = line.strip().split(":")
                usuarioEsenha[usuario] = senha
    except FileNotFoundError:
        pass

    try:
        with open("livros.txt", "r") as file:
            for line in file:
                titulo, autor, ano = line.strip().split(":")
                livros[titulo] = {'autor': autor, 'ano_publicacao': ano}
    except FileNotFoundError:
        pass

def gerenciar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")

    usuarioEsenha[nome_usuario.capitalize()] = senha
    print("Usuário", nome_usuario, "registrado com sucesso!")

def login():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome_usuario.capitalize() in usuarioEsenha and usuarioEsenha[nome_usuario.capitalize()] == senha:
        print("Login feito com sucesso!")
    else:
        print("Nome de usuário ou senha incorreta!")

def cadastrar_livros():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    livros[titulo] = {'autor': autor, 'ano_publicacao': ano}
    print("Livro registrado com sucesso!")

def retornar_usuarios():
    print("Usuários registrados:")
    for usuario, senha in usuarioEsenha.items():
        senha_oculta = "*" * len(senha)  # Substitui a senha por asteriscos
        print(f"Usuário: {usuario}, Senha: {senha_oculta}")

def retornar_livros():
    print("Livros cadastrados:")
    for livro, detalhes in livros.items():
        print(f"Título do livro: {livro}, Autor: {detalhes['autor']}, Ano: {detalhes['ano_publicacao']}")

def salvar_dados():
    with open("usuarios.txt", "w") as file:
        for usuario, senha in usuarioEsenha.items():
            file.write(f"{usuario}:{senha}\n")

    with open("livros.txt", "w") as file:
        for titulo, detalhes in livros.items():
            autor = detalhes['autor']
            ano = detalhes['ano_publicacao']
            file.write(f"{titulo}:{autor}:{ano}\n")

def main():
    carregar_dados()

    while True:
        print("\n*** Menu ***")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Cadastrar livro")
        print("4. Mostrar usuários cadastrados")
        print("5. Mostrar livros cadastrados")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciar_usuario()
            salvar_dados()
        elif opcao == "2":
            login()
        elif opcao == "3":
            cadastrar_livros()
            salvar_dados()
        elif opcao == "4":
            retornar_usuarios()
        elif opcao == "5":
            retornar_livros()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
