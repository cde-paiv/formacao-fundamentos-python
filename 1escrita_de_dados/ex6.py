#Por defeito só são apresentadas 6 casas decimais
print("%f" % 5.1234567890)
#Neste caso, são retornadas 5 casa decimais
print("%.5f" % 5.1234567890) 
#Neste caso no máximo 9 valores sendo 5 decimais
print("%9.5f" % 5.1234567890)
#Neste caso, no máximo 15 valores sendo 5 decimais, para atingir os 15
#coloca zeros à esquerda
print("%015.5f" % 5.1234567890)
#É deixado um espaço em branco à esquerda para que o alinhamento seja
#mantido, quando há numeros negativos
print("% 9f" % 5.1234567890)
print("% 9f" % -5.1234567890)
#Os números positivos são apresentados com o sinal "+"
print("%+9f" % 5.1234567890)
print("% 9f" % -5.1234567890)