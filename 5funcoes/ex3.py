def maior(x, y):
    if x > y:
        return x
    else:
        return y
    
a = int(input("digite o primeiro valaor "))
b = int(input("digite o segundo valor "))

resultado = maior(a , b)
print("o maior valor e: ", resultado)