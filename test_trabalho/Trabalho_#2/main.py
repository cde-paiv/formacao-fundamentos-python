import biblioteca

def menu():
    while True:
        print("\n--- Gestão de Biblioteca ---")
        print("1. Listar livros")
        print("2. Adicionar livro")
        print("3. Atualizar livro")
        print("4. Remover livro")
        print("5. Procurar por ISBN")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca.listar_livros()
        elif opcao == "2":
            biblioteca.adicionar_livro()
        elif opcao == "3":
            biblioteca.atualizar_livro()
        elif opcao == "4":
            biblioteca.remover_livro()
        elif opcao == "5":
            biblioteca.procurar_por_isbn()
        elif opcao == "0":
            print(" Encerrando gestão da biblioteca.")
            break
        else:
            print(" Opção inválida.")

menu()
