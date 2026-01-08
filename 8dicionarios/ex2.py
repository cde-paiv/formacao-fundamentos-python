d1 = {
    "one": 11,
    "two": 22,
    "three": 33,
    "four": 44,
    "five": 55
}

#a)
def escreve_dicionario(d):
    for k in d:
        print("Chave:", k, "→ Valor:", d[k])

#b)
def calcula_media(d):
    soma = 0
    for v in d.values():
        soma += v
    return soma / len(d)

#c)
def conta_valores(d, n2):
    cont = 0
    for v in d.values():
        if v > n2:
            cont += 1
    return cont

escreve_dicionario(d1)
print("Média dos valores:", calcula_media(d1))
print("Valores maiores que 30:", conta_valores(d1, 30))
