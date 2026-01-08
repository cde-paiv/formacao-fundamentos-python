valor = int(input("Introduza o valaor: "))
soma = 0
for i in range(1, valor + 1):
    soma += i
    
print(f"*** A soma dos numeros inteiros ate {valor}: {soma} ***")

#a)
def somar_ate(valor_soma):
    soma = 0
    for i in range(1, valor_soma + 1):
        soma += i
    return soma

valor = int(input("Introduza o valaor: "))
resultado = somar_ate(valor)
print(f"*** A soma dos numeros inteiro ate {valor}: {resultado} ***")

#b)
def somar_while(valor):
    soma = 0
    i = 0
    while i <= valor:
        soma += i
        i += 1
    return soma
valor = int(input("introduza o valor: "))
resultado = somar_while(valor)
print(f"*** A soma dos numeros inteiro ate {valor}: {resultado} ***")
