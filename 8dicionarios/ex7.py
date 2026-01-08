pessoas = {
    1: {"cc": "12312344", "nome": "Alfredo", "idade": "22"},
    2: {"cc": "72365912", "nome": "Diana", "idade": "25"}
}

def listar_pessoas():
    for id, dados in pessoas.items():
        print(f"\nPessoa ID: {id}")
        for key in dados:
            print(f"{key}: {dados[key]}")

def adicionar_pessoa():
    novo_id = max(pessoas.keys()) + 1 if pessoas else 1
    cc = input("CC: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    pessoas[novo_id] = {"cc": cc, "nome": nome, "idade": idade}
    print("Pessoa adicionada com sucesso.")

def atualizar_pessoa():
    id = int(input("Digite o ID da pessoa a atualizar: "))
    if id in pessoas:
        cc = input("Novo CC: ")
        nome = input("Novo Nome: ")
        idade = input("Nova Idade: ")
        pessoas[id] = {"cc": cc, "nome": nome, "idade": idade}
        print("Dados atualizados.")
    else:
        print("ID não encontrado.")

def remover_pessoa():
    id = int(input("Digite o ID da pessoa a remover: "))
    if id in pessoas:
        del pessoas[id]
        print("Pessoa removida.")
    else:
        print("ID não encontrado.")

def consultar_por_cc():
    cc_busca = input("Digite o número de CC para pesquisar: ")
    for id, dados in pessoas.items():
        if dados["cc"] == cc_busca:
            print(f"\nPessoa encontrada (ID {id}):")
            for key in dados:
                print(f"{key}: {dados[key]}")
            return
    print("Pessoa não encontrada com esse CC.")

# Menu principal
while True:
    print("\nGestão de Pessoal")
    print("1. Listar pessoas")
    print("2. Adicionar pessoa")
    print("3. Atualizar pessoa")
    print("4. Remover pessoa")
    print("5. Consultar por CC")
    print("0. Sair")
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        listar_pessoas()
    elif opcao == "2":
        adicionar_pessoa()
    elif opcao == "3":
        atualizar_pessoa()
    elif opcao == "4":
        remover_pessoa()
    elif opcao == "5":
        consultar_por_cc()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
