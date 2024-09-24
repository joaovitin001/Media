
alunos = {}

while True:
    print()
    print(15*"=", "Menu", 15*"=")
    print("1. Cadastrar aluno")
    print("2. Exibir médias")
    print("3. Sair")
    print(36*"=")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ").upper()
        n1 = float(input("Digite a primeira nota do aluno: "))
        n2 = float(input("Digite a segunda nota do aluno: "))
        n3 = float(input("Digite a terceira nota do aluno: "))

        alunos[nome] = {f"Nome": nome, "Nota 1": n1, "Nota 2": n2, "Nota 3": n3}

        print(f"Aluno {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if alunos:
            print("\n--- Lista de Alunos Cadastrados---")

            for nome, dados in alunos.items():
                media = (dados["Nota 1"] + dados["Nota 2"] + dados["Nota 3"]) / 3
                print(f"Nome: {dados["Nome"]}, Média: {media:.1f}")
        else:
            print("Nenhum aluno cadastrado")

    elif opcao == "3":
        print("Saindo do sistema!")
        break