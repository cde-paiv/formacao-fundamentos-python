numeros_por_extenso = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez"
}

# Solicita o valor ao utilizador
valor = int(input("Introduza um valor até 10: "))

# Verifica se o valor está no intervalo permitido
if 0 <= valor <= 10:
    print(f"O valor introduzido foi o {numeros_por_extenso[valor]}")
else:
    print("Valor inválido. Por favor, introduza um número entre 0 e 10.")
