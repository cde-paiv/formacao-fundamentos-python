a = float(input("Introduzir um valor: "))
b = float(input("Introduzir outro valor: "))

print("\nResultado:")
if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("Os dois valores são iguais.")
