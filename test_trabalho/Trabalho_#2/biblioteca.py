livros = {}

def validar_isbn(isbn):
    return isbn.count("-") == 2 and all(part.isdigit() for part in isbn.split("-"))

def validar_ano(ano):
    return ano.isdigit() and int(ano) > 0

def obter_data_manual():
    dia = input("Dia (dd): ")
    mes = input("Mês (mm): ")
    ano = input("Ano (yyyy): ")
    if len(dia) == 1: dia = "0" + dia
    if len(mes) == 1: mes = "0" + mes
    return f"{dia}/{mes}/{ano}"

def listar_livros():
    if not livros:
        print("Nenhum livro registrado.")
    else:
        for isbn, dados in livros.items():
            print(f"\nISBN: {isbn}")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")

def adicionar_livro():
    try:
        isbn = input("ISBN (formato XXX-XXX-XXX): ")
        if not validar_isbn(isbn):
            print("Formato inválido de ISBN.")
            return
        if isbn in livros:
            print("Esse ISBN já existe.")
            return
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")
        if not validar_ano(ano):
            print("Ano inválido.")
            return
        data = obter_data_manual()
        livros[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "data_registo": data
        }
        print(" Livro adicionado.")
    except Exception as e:
        print("Erro ao adicionar livro:", e)

def atualizar_livro():
    isbn = input("ISBN do livro a atualizar: ")
    if isbn in livros:
        titulo = input("Novo título: ")
        autor = input("Novo autor: ")
        ano = input("Novo ano: ")
        if not validar_ano(ano):
            print("Ano inválido.")
            return
        data = obter_data_manual()
        livros[isbn].update({
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "data_registo": data
        })
        print(" Livro atualizado.")
    else:
        print("ISBN não encontrado.")

def remover_livro():
    isbn = input("ISBN do livro a remover: ")
    if isbn in livros:
        del livros[isbn]
        print(" Livro removido.")
    else:
        print("ISBN não encontrado.")

def procurar_por_isbn():
    isbn = input("ISBN para procurar: ")
    if isbn in livros:
        print(f"\n Livro encontrado: {isbn}")
        for k, v in livros[isbn].items():
            print(f"{k.capitalize()}: {v}")
    else:
        print("Livro não encontrado.")
