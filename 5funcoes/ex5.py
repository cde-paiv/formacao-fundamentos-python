def divisao(x, y):
    if y != 0:
        div = x / y
        return div
    else:
        return None

v1 = int(input("Digite o pirmeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

div = divisao(v1, v2)

print("o valor da divisao e: ", div)