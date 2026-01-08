def print_array(arr):
    for x in arr:
        print(x)

temperaturas = [10, 21, 12, 22, 22]
print("Elementos iniciais do array, com dimensão:", len(temperaturas))
print_array(temperaturas)

print("Adicionar um novo elemento no array")
temperaturas.insert(3, 21)
print_array(temperaturas)

print("Adicionar um novo elemento no array")
temperaturas.insert(3, 21)
print_array(temperaturas)

temperaturas.pop(0)
print("Eliminar elemento de index 0")
print_array(temperaturas)

temperaturas.remove(22)
print("Eliminar primeira ocorrência do valor 22")
print_array(temperaturas)

#a)
print("Quantidade de elementos:", len(temperaturas))

#b)
maior = temperaturas[0]
for x in temperaturas:
    if x > maior:
        maior = x
print("valor maximo: ", maior)

#c)
contagem = 0
for x in temperaturas:
    if x == 22:
        contagem += 1
print("ocorrencia de 22: ", contagem)