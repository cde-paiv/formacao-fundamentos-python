def welcome():
    print("***************************")
    print("*****  Programa DOBRO  ****")
    print("***************************")
    

def double_number(x):
    d = 2 * x
    return d

welcome()

valor = int(input("qual valor queres calcular o dobro? "))
print("o dobro de", valor, "=", double_number(valor))