def calcular_media_e_menor_tempo(v1, v2, v3, v4, v5):
    tempos = [v1, v2, v3, v4, v5]
    media = sum(tempos) / len(tempos)
    menor = min(tempos)
    print(f" Menor tempo individual: {menor:.2f} segundos")
    return media

def ler_tempos_piloto(numero_piloto):
    print(f"\n Introduza os tempos do Piloto {numero_piloto}:")
    tempos = []
    for i in range(1, 6):
        tempo = float(input(f"Volta {i}: "))
        tempos.append(tempo)
    return calcular_media_e_menor_tempo(*tempos)

medias = []

for i in range(1, 4):
    media = ler_tempos_piloto(i)
    medias.append(media)

vencedor = medias.index(min(medias)) + 1

print(f"\n Piloto vencedor: Piloto {vencedor} com menor tempo médio!")
print(" Médias de cada piloto:")
for i, m in enumerate(medias, 1):
    print(f"Piloto {i}: {m:.2f} segundos")
