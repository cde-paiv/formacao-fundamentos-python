dados = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Lisboa"
}

#a)
dados["profissão"] = "engenheira"

#b)
dados["idade"] = 27

#c)
print("apelido" in dados)  # False
print("nome" in dados)     # True

#d)
dados.pop("cidade")