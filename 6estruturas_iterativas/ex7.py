def somar_valores():
    soma = 0
    while True:
        valor = int(input("digite um valor (0 para terminar): "))
        if valor == 0:
            break
        soma += valor
    print(f"soma total:  {soma}")
    
somar_valores()