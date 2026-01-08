def valida_email(txt):
    pos1 = txt.find("@")
    if( len(txt) > 8 and pos1 > 3):
        return True
    else:
        return False
    
email = input("introduzir email: ")

a = valida_email(email)
if (a == True):
    print("email valido")
else:
    print("email invalido")