temperaturas = [12, 19, 21, 17, 18, 14]
temperaturas[0] = 11
print("Novo valor para a posição de índice 0:", temperaturas[0])
temperaturas.insert(6, 13)
print(temperaturas)

#a)
print("Quantidade de elementos:", len(temperaturas))

#b)
def imprime_elementos(lista):
    for elemento in lista:
        print(elemento)

imprime_elementos(temperaturas)

#c)
def imprime_pares(lista):
    for elemento in lista:
        if elemento % 2 == 0:
            print("imprimir pares ", elemento)

imprime_pares(temperaturas)

#d)
def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

print("Soma:", soma_elementos(temperaturas))

#e)
def media_elementos(lista):
    return soma_elementos(lista) / len(lista)

print("Média:", media_elementos(temperaturas))

#f)
def procura_elementos(lista, valor):
    contagem = 0
    for elemento in lista:
        if elemento == valor:
            contagem += 1
    return contagem

print("Ocorrências do número 14:", procura_elementos(temperaturas, 14))