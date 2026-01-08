number = int(input("introduzir um numero entre 100 e 500 "))

while number < 100 or number > 500:
    print("nunero incorreto, por favor introduza o numero correto ")
    number = int(input("introduzir um numero entre 100 e 500"))

print("parabens, introduziu o numero correto", number)