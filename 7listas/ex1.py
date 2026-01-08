#a)
temperaturas = [12, 19, 21, 17, 18, 14]
temperaturas[0] = 11
print("novo valor para a posiçao de indice 0:", temperaturas[0])


#b)
temperaturas = [12, 19, 21, 17, 18, 14]
temperaturas.append(30)
print("novo valor para a lista:", temperaturas[6])

#c)
temperaturas = [12, 19, 21, 17, 18, 14]
def soma_2(x):
    s = x[0] + x[1]
    return s

result = soma_2(temperaturas)
print("a soma dos dois primeiros: ", result)

#d)
temperaturas = [12, 19, 21, 17, 18, 14]
def ultima(list):
    a = list[ len(temperaturas) - 1]
    return a

last = ultima(temperaturas)
print("o ultimo elemento da lista e: ", last)

#e)
def adiciona(l):
    l.append(100)
    
print("temperatura", temperaturas)

lista2 = [2, 20]
print("lista2", lista2)

adiciona(temperaturas)

adiciona(lista2)

print("temperatura", temperaturas)
print("lista2", lista2)

#f)
temperaturas = [12, 19, 21, 17, 18, 14]
for i in range(0, 6):
    print("temperaaturas ", temperaturas[i])