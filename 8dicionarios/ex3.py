a = {'joe': 85, 'peter': 88, 'jack': 90}
b = dict(joe=90, peter=85, jack=88)
c = dict([('joe', 90), ('peter', 85), ('jack', 95)])

a['Walter'] = 76
b['Walter'] = 77
c['Walter'] = 78

#a) remover a chave “joe” do dicionário “a” 
a.pop("joe")

#b)adicionar o valor “60” com a chave “maria” ao dicionário “a”
a["maria"] = 60

#c)atualizar a chave “jack” com o valor “88” ao dicionário “a”
a["jack"] = 88

#d)imprimir a quantidade de elementos do dicionário “a” 
print("Quantidade de elementos em 'a':", len(a))

#e)Função valida_valor(dicionario, valor) 
# que verifica se o valor existe no dicionário:
def valida_valor(dic, valor):
    for v in dic.values():
        if v == valor:
            return True
    return False

if valida_valor(a, 88):
    print("O valor 88 está no dicionário.")
    
#f)listar as chaves do dicionário “a” cujos valores se repetem
def chaves_valores_repetidos(dic):
    vistos = []
    repetidos = []
    for k, v in dic.items():
        if v in vistos:
            repetidos.append(k)
        else:
            vistos.append(v)
    return repetidos

print("Chaves com valores repetidos:", chaves_valores_repetidos(a))

#g)eliminar o dicionário “b”
del b