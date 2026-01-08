def converter(temp, origem, destino):
    if origem == "c" and destino == "f":
        return temp * 9/5 + 32
    if origem == "c" and destino == "k":
        return temp + 273.15
    if origem == "f" and destino == "c":
        return (temp - 32) * 5/9
    if origem == "f" and destino == "k":
        return (temp - 32) * 5/9 + 273.15
    if origem == "k" and destino == "c":
        return temp - 273.15
    if origem == "k" and destino == "f":
        return (temp - 273.15) * 9/5 + 32
    return temp

def main():
    while True:
        print("\nEscalas: c = Celsius | f = Fahrenheit | k = Kelvin")
        origem = input("Escala de entrada: ").lower()
        destino = input("Escala de saída: ").lower()
        temp = float(input("Valor da temperatura: "))
        resultado = converter(temp, origem, destino)
        print(f"{temp} {origem.upper()} = {resultado:.2f} {destino.upper()}")
        if input("Nova conversão? (s/n): ").lower() != "s":
            break

main()
