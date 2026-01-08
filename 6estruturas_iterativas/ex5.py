valor = int(input("introduza um valor: "))
for i in range(2, valor + 1, 2):
    print(f"{i} --> par")
    
#a)
def mostrar_pares(valor):
    for i in range(2, valor + 1, 2):
        print(f"{i} --> par")
        
valor = int(input("introduza um valor: "))
mostrar_pares(valor)


#b)
def pares_while(valor):
    i = 2
    while i <= valor:
        print(f"{i} --> par")
        i += 2

valor = int(input("introduza um valor: "))
pares_while(valor)