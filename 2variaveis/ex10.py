str_url = "http://pythonworld.com/course"

# Substitui ".com" por ".net"
s2 = str_url.replace(".com", ".net")
print("str_url:", str_url)
print("s2:", s2)

# Conta quantas vezes "/" aparece
count = str_url.count("/")
print("Contagem de '/' :", count)

# Encontra a posição da palavra "python"
pos = str_url.find("python")
print('Posição de "python" :', pos)
