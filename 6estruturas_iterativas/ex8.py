import random

def jogo_adivinha():
    valor_aleatorio = random.randint(1, 100)
    tentativa = 0
    
    while True:
        tentativa = int(input("tente adivinhar o numero entre 1 e 100:  "))
        if tentativa < valor_aleatorio:
            print("muito baixo, tente novamente")
        elif tentativa > valor_aleatorio:
            print("muito alto, tente novamente")
        else:
            print("parabens! acertou o numero!")
            break
        
jogo_adivinha()